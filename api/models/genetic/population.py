import numpy as np
from data.models.core.genetic.individual import Individual
from data.models.core.matrix import Matrix
from copy import deepcopy


from constants.cts import (
    CURRENT, EMPTY_STR, FUTURE, INITIAL, STR_ONE, STR_ZERO,
    be_tensor, le_tensor,
)


class Population:
    ''' Class Population is used to cause effects over the individuals. '''

    def __init__(self) -> None:
        self._individuals: list[Individual] = []
        self._channels: dict[str, list[str]] = None
        self._subtensor: list[Matrix] = list()

    def get_size(self) -> int:
        return len(self._individuals)

    def get_individuals(self) -> list[Individual]:
        return deepcopy(self._individuals)

    def set_individuals(self, individuals: list[Individual]) -> None:
        self._individuals = individuals

    def set_channels(self, channels: dict[str, list]) -> None:
        self._channels = channels

    def set_subtensor(self, sub_tensor: list[Matrix]) -> None:
        self._subtensor = sub_tensor

    def get_subtensor(self) -> list[Matrix]:
        return deepcopy(self._subtensor)

    def generate_individuals(
        self, pop_size, channels
    ) -> None:
        '''
        INPUT -> ABC|DE: cms1 = [011.01]
                                (BC.E)(A.D)
        '''

        chromosomes: np.ndarray = self.generate_k_cms(
            len(self._channels[FUTURE]),
            len(self._channels[CURRENT]),
            pop_size
        )
        # chromosomes = [
        #     np.array([0, 1, 0, 0, 0, 0], dtype=bool),
        #     np.array([1, 0, 1, 1, 1, 1], dtype=bool),
        # ]
        # Validamos que los cromosomas generados sean soluciones
        validated_cms = self.validate_cms(chromosomes)

        # Generamos las distribuciones para cada uno de nuestros cromosomas
        distributions = [
            self.update_distribution(chr, channels[INITIAL])
            for chr in validated_cms
        ]
        individuals: list[Individual] = [
            Individual(chr, dist)
            for chr, dist in zip(validated_cms, distributions)
        ]
        # count = 0
        # for ind in individuals:
        #     if np.sum(ind.get_dist()) != 1.0:
        #         count += 1
        self._individuals = individuals

    # (AC|ABC)(B|0) ->[010.000]
    #   Individual: [False  True False False False False] - 1.0
    #   [[0.    0.    0.    0.    0.375 0.125 0.375 0.125]]

    def update_distribution(
        self, chr: np.ndarray, initial_state: str
    ) -> np.ndarray:
        """
                            F0, F2, F3, F5
            C1, C2, C4, C5

            {0: [0, 2, 3, 5], 1: [1, 2, 4, 5]} :: 0 is future, 1 is current

            Así mismo, los enteros de los canales son las claves para acceder a los índices con los cuales se seleccionarán las matrices del tensor.

        """
        primal_f = list()
        primal_c = list()

        dual_f = list()
        dual_c = list()

        future = self._channels[FUTURE]
        current = self._channels[CURRENT]

        # Miramos en el futuro:
        for idx, channel in enumerate(future):
            if chr[idx]:
                primal_f.append(channel)
            else:
                dual_f.append(channel)

            # primal_f.append(channel) \
            #     if chr[idx] \
            #     else dual_f.append(channel)
            # if chr[idx]:
            #     f_primal.append(channel)
            # else:
            #     f_dual.append(channel)

        # Anotamos el tamaño del futuro
        f_size: int = len(future)

        for idx, channel in enumerate(current):
            if chr[idx + f_size]:
                primal_c.append(channel)
            else:
                dual_c.append(channel)

        # Ahora viene un posible paralelismo, donde marginalizamos el tensor #

        union_product = None
        subtensor = self.get_subtensor()

        # No debemos marginalizar si no hay futuros
        if len(primal_f) == 0:
            # Generamos la partición primal y dual
            # unit_primal = np.ndarray([1], dtype=float)
            serie_dual: list = list()

            # Debemos marginalizar la dual
            dual_cstate_key = EMPTY_STR.join([
                STR_ONE if ci in dual_c
                else STR_ZERO for ci in current
            ])
            # Obtenemos la clave de inicialización
            dual_cinit_key = EMPTY_STR.join([
                initial_state[ci]
                for ci in dual_c
            ])
            # Almacenamos las series seleccionadas
            for matrix in subtensor:
                mar_matrix = matrix.margin_row(dual_cstate_key, be=True)
                serie_dual.append(
                    mar_matrix
                    if dual_cinit_key == EMPTY_STR
                    else matrix.select_series(dual_cinit_key)
                )
            # Hacemos producto tensor little endian entre las series
            subtensor_product = be_tensor(serie_dual)
            # Este paso lo podemos omitir
            # union_product = be_tensor([unit_primal, subtensor_product])
            union_product = subtensor_product
            # return subtensor_product

        elif len(dual_f) == 0:
            # return []
            # unit_dual = np.ndarray([1], dtype=float)
            serie_primal: list = list()

            # Debemos marginalizar la primal
            primal_cstate_key = EMPTY_STR.join([
                STR_ONE if ci in primal_c
                else STR_ZERO for ci in current
            ])
            # Obtenemos la clave de inicialización
            primal_cinit_key = EMPTY_STR.join([
                initial_state[ci]
                for ci in primal_c
            ])
            # Almacenamos las series seleccionadas
            for matrix in subtensor:
                mar_matrix = matrix.margin_row(primal_cstate_key, be=True)
                serie_primal.append(
                    mar_matrix
                    if primal_cinit_key == EMPTY_STR
                    else matrix.select_series(primal_cinit_key)
                )

            # Hacemos producto tensor little endian entre las series
            subtensor_product = be_tensor(serie_primal)
            # Este paso lo podemos omitir
            # union_product = be_tensor([subtensor_product, unit_dual])
            union_product = subtensor_product
            # return subtensor_product
        else:
            # La lógica de selección es entre la combinación de la clave en los canales y si está en el indice
            serie_primal: list = list()
            serie_dual: list = list()

            cprimal_state_key = EMPTY_STR.join([
                STR_ONE if ci in primal_c
                else STR_ZERO for ci in current
            ])
            cprimal_init_key = EMPTY_STR.join([
                initial_state[ci]
                for ci in primal_c
            ])

            cdual_state_key = EMPTY_STR.join([
                STR_ONE if ci in dual_c
                else STR_ZERO for ci in current
            ])
            cinit_dual_key = EMPTY_STR.join([
                initial_state[ci]
                for ci in dual_c
            ])

            # Marginalizamos ambos tensores
            for i, matrix in enumerate(subtensor):
                # Vamos a hacer una iteración cruzada
                if future[i] in primal_f:
                    mar_matrix = matrix.margin_row(cprimal_state_key, be=True)
                    serie_primal.append(
                        mar_matrix
                        if cprimal_init_key == EMPTY_STR
                        else matrix.select_series(cprimal_init_key)
                    )
                else:
                    mar_matrix = matrix.margin_row(cdual_state_key, be=True)
                    serie_dual.append(
                        mar_matrix
                        if cinit_dual_key == EMPTY_STR
                        else matrix.select_series(cinit_dual_key)
                    )

            # Hacemos producto tensor little endian entre las series
            subtensor_primal = be_tensor(serie_primal)
            subtensor_dual = be_tensor(serie_dual)
            # Este paso lo podemos omitir
            union_product = be_tensor([subtensor_primal, subtensor_dual])

        if union_product is None:
            raise ValueError('Union product is None')
        elif len(union_product) == 0:
            raise ValueError('Union product is empty')
        elif len(*union_product) != 2**len(future):
            # El número de matrices de el tamaño horizontal
            raise ValueError(
                f'Union product is not the right size: {len(*union_product)}'
            )
        elif np.sum(union_product) != 1.0:
            raise ValueError('Union product is not normalized')

        return union_product

    def validate_cms(self, cms: list[np.ndarray]) -> list[np.ndarray[np.bool_]]:
        for chr in cms:
            all_true = np.all(chr, axis=0)
            all_false = np.all(~chr, axis=0)

            if all_false or all_true:
                rnd_idx = np.random.randint(0, len(chr))
                chr[rnd_idx] = ~chr[rnd_idx]
        return cms

    def generate_k_cms(self, m: int, n: int, k: int) -> list[np.ndarray[np.bool_]]:
        # Crear un array de enteros que representa los números binarios

        total_combinaciones = 2 ** (n+m-1) - 1
        mini_combs: int = min(k, total_combinaciones)

        # return self.generar_random(n, m)

        if k > total_combinaciones:
            # Si las combinaciones brindadas por el usuario superan el tamaño máximo de combinaciones ofrecidas por fuerza bruta, usamos la primera forma (primera línea de combinaciones)
            return self.generate_cms(m, n)
        else:
            # Crear un arreglo de enteros desde 0 hasta mini_combs - 1
            enteros = np.arange(mini_combs, dtype=np.uint32)
            # Convertir cada entero a una matriz de bits booleana
            combinaciones_binarias = (
                (enteros[:, None] & (1 << np.arange(n + m))) > 0)
            return combinaciones_binarias

    def generate_random(self, n: int, m: int) -> np.ndarray:
        # Creamos un arreglo de flotantes de tamaño n + m
        floating = np.random.randint(0, 2, size=(n + m, n + m))
        # Lo volvemos uno de booleanos con la condición de que el valor > 0.5
        return floating > 0.5

    def generate_cms(self, m: int, n: int) -> np.ndarray:
        # Número total de combinaciones binarias para n bits
        total_combinaciones = 2 ** n
        # Crear un array de enteros que representa los números binarios
        enteros = np.arange(total_combinaciones, dtype=np.uint8)
        # Convertir los enteros a su representación binaria
        binarios = ((enteros[:, None] & (1 << np.arange(n))) > 0)
        # Crear un array de valores True de tamaño (total_combinaciones, m)
        trues = np.ones((total_combinaciones, m), dtype=bool)
        # Concatenar los valores True al inicio de cada fila del array binario
        return np.hstack((trues, binarios))
