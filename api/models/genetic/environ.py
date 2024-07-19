import random
import numpy as np
from numpy.typing import NDArray

from constants.genetic import CROSS_RATE, DECAY, INIT_POP_SIZE, MAX_GENS, MAX_STREAK, PARENTS_NUM
from api.models.genetic.individual import Individual
from api.models.genetic.population import Population
from api.models.structure import Structure

from icecream import ic
from utils.consts import ACTUAL, EFFECT, INFTY_POS, ROWS_IDX
from utils.funcs import emd

from server import conf
from api.models.genetic.recorder import rec


class Environ:
    """Class Environ is used to evolve a population.
    This is achieved using the genetic algorithm definiton of genetic operators. ."""

    def __init__(
        self,
        ctrl_params: dict[str, float | int],
        structure: Structure,
        distribution: NDArray[np.float64],
        concept: tuple[list[int], list[int]],
        dual: bool,
    ) -> None:
        self.__ctrl_params: dict[str, float | int] = ctrl_params
        # self.__structure: Structure = structure
        self.__distrib: NDArray[np.float64] = distribution

        # self.__effect: list[int] = concept[EFFECT]
        # self.__causes: list[int] = concept[ACTUAL]

        self.__population: Population = Population(distribution, concept, structure)
        # self.__target_dist: NDArray[np.float64] = None
        self.__dual: bool = dual

    def evolve(self) -> Individual:
        """Method evolve is used to evolve the population."""
        # ! Inicialización de la población ! #
        ic(self.__population.get_concept())
        self.__population.generate_individuals(self.__ctrl_params[INIT_POP_SIZE])

        # ! Computar función de evaluación para todo individuo. ! #
        individuals: list[Individual] = self.__population.get_individuals()
        for init_ind in individuals:
            ind_fitness = self.compute_fitness(init_ind.get_dist())
            init_ind.set_fit(ind_fitness)
        self.__population.set_individuals(individuals)
        [ic(ind) for ind in individuals]

        # ! WHILE incumpla la condición de terminación DO ! #
        finishing_condition: bool = False
        while not finishing_condition:
            # ! Seleccionar individuos para cruzarlos ! #
            inds = self.tournament_selection(self.__ctrl_params[PARENTS_NUM])

            # ! Cruzar individuos seleccionados. ! #
            crossed_cms: list[NDArray[np.bool_]] = self.crossover(inds)
            ic(crossed_cms)

            # ! Mutar algunos individuos (+infactibles) ! #
            mutated_indivs: list[Individual] = self.mutate_cms(crossed_cms)

            # ! Testear la nueva generación. ! #
            finishing_condition = self.test_population()

            # ! Reemplazar la población actual con la nueva generación ! #
            self.replace_population(mutated_indivs)
            [ic(mut_ind) for mut_ind in mutated_indivs]

        return rec.get_best_individual()

    def replace_population(self, individuals: list[Individual]) -> None:
        # Computamos la función de eficiencia para cada individuo
        for ind in individuals:
            fitness = self.compute_fitness(ind.get_dist())
            ind.set_fit(fitness)

        self.__population.set_individuals(individuals)

    def test_population(self) -> bool:
        """Cuando se cumple la condición de terminación, se retorna True y se termina la búsqueda. Se pone a prueba la población actual."""
        m: int = len(self.__population.get_concept()[EFFECT])
        n: int = len(self.__population.get_concept()[ACTUAL])

        # Si ha alcanzado el tamaño del espacio de búsqueda, debe terminar #
        # max_generations = 2**(m+n-1)-1
        record_gens: int = rec.get_last_generation()
        if record_gens >= self.__ctrl_params[MAX_GENS]:
            return True

        min_fitness: float = INFTY_POS
        best_ind: Individual = None

        for ind in self.__population.get_individuals():
            ind_fitness = ind.get_fitness()
            # ind.set_fitness(self.compute_fitness(ind.get_dist()))
            if ind_fitness == 0:
                # Si hay un individuo con distribución de 0, es la mejor solución válida #

                rec.add_best_individual(ind)
                return True
            elif ind_fitness < min_fitness:
                # Si no es el mejor irá tomando el mínimo de la población #
                best_ind = ind
                min_fitness = ind_fitness

        if self.check_loses():
            return True

        rec.add_best_individual(best_ind)
        return False

    def check_loses(self) -> bool:
        #  Si se detecta que hubo una racha de individuos sin mejora (decaimiento), se termina la búsqueda #
        inds = rec.get_bests_individuals()
        inds_len: int = len(inds)
        # Validamos que no hayan suficientes generaciones para que siquiera haya una racha
        if inds_len < self.__ctrl_params[DECAY]:
            return False
        # Recorremos
        streak: int = 0
        all_fits: list[float] = [-1.0 for _ in inds]
        all_fits[0] = inds[0].get_fitness()
        for i in range(1, inds_len):
            streak += 1
            all_fits[i] = inds[i].get_fitness()
            if all_fits[i] > all_fits[i - 1]:
                streak = 0

        return streak > self.__ctrl_params[DECAY]

    def mutate_cms(self, crossed_cms: list[NDArray]) -> list[Individual]:
        # validated
        len_exc_cms = len(crossed_cms) - 1
        if len_exc_cms + 1 == 0:
            raise ValueError('No individuals to mutate')
        individuals_to_mutate = random.randint(1, len_exc_cms)

        sample_inds = random.sample(range(len_exc_cms), individuals_to_mutate)

        # Vamos a mutar un gen en cada individuo de la muestra seleccionada
        for idx in sample_inds:
            chr: NDArray[np.bool_] = crossed_cms[idx][0]
            rand_gen_idx = random.randint(0, len(chr) - 1)
            # Mutar el gen cambiando su valor booleano
            chr[rand_gen_idx] = ~chr[rand_gen_idx]

        unpacked_cms = [chr.flatten() for chr in crossed_cms]
        validated_cms = self.__population.validate_cms(unpacked_cms)
        dists: list[NDArray] = self.__population.update_distribution(validated_cms)

        individuals: list[Individual] = list()
        for chr, dist in zip(validated_cms, dists):
            individuals.append(Individual(chr, dist))

        for ind in individuals:
            ind.set_fit(self.compute_fitness(ind.get_dist()))

        return individuals

    def crossover(self, individuals: list[Individual]) -> list[NDArray[np.bool_]]:
        []
        childs = [
            # Cruzamos el primer y último individuo del arreglo de padres
            self.cross(individuals[0], individuals[-1])
        ] + [
            # Iteramos por cada pareja de individuos del arreglo saliente mediante torneo, cruzaremos estos esquemas de padres y generaremos un hijo
            self.cross(x, y)
            for x, y in zip(individuals, individuals[1:])
        ]
        flattened_childs = [child for sublist in childs for child in sublist]
        # Ya que en el torneo se seleccionan 02 padres, se generan 02 hijos por cada pareja de padresñ
        return flattened_childs

    def cross(self, prim_parent: Individual, dual_parent: Individual) -> list[NDArray[np.bool_]]:
        # Generar un array de números aleatorios entre 0 y 1
        random_floats = np.random.rand(len(prim_parent.get_chr()))

        # Generamos una máscara de cruza uniforme
        cross_rate: float = self.__ctrl_params[CROSS_RATE]
        crossing_mask: NDArray = random_floats <= (cross_rate)

        # Seleccionamos 02 padres
        fathers: list[Individual] = [prim_parent, dual_parent]

        # [
        #     for chr in fathers
        # ]

        prim_cms: NDArray[np.bool_] = np.zeros((1, len(prim_parent.get_chr())), dtype=bool)
        dual_cms: NDArray[np.bool_] = np.zeros((1, len(dual_parent.get_chr())), dtype=bool)
        for i, b in enumerate(crossing_mask):
            idx_prim: int = int(b)
            idx_dual: int = int(not b)

            chr_prim = fathers[idx_prim].get_chr()
            chr_dual = fathers[idx_dual].get_chr()

            prim_cms[ROWS_IDX][i] = chr_prim[i]
            dual_cms[ROWS_IDX][i] = chr_dual[i]

        return [prim_cms, dual_cms]

    def tournament_selection(self, r: int) -> list[Individual]:
        popul: Population = self.__population
        winner_parents: list[Individual] = list()
        # Seleccionar la mitad de la población como padres
        num_parents = popul.get_size() // r
        individuals = popul.get_individuals()

        for _ in range(num_parents):
            tournament: list[Individual] = random.sample(individuals, r)
            winner: Individual = min(tournament, key=lambda ind: ind.get_fitness())
            winner_parents.append(winner)

            # Para evitar el decremento de la población, añadimos esquemas del padre para dar aleatoriedad luego en el cruzamiento
            # father_schemas: int = random.randint(0, PARENTS_NUM-1)
            # father_schemas: int = random.randint(0, 1)
            # for _ in range(father_schemas):
            #     winner_parents.append(winner)

        # [
        #     for m in selected_parents
        # ]
        return winner_parents

    def compute_fitness(self, distribution: NDArray[np.float64]) -> float:
        return emd(
            distribution,
            self.__distrib,
            le=conf.little_endian,
        )
