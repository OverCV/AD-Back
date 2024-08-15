import copy
from typing import OrderedDict
import numpy as np
from api.models.structure import Structure
from api.schemas.structure import StructureResponse

from numpy.typing import NDArray
import itertools as it

from icecream import ic

from utils.consts import BASE_2, COLS_IDX, STR_ONE
from utils.funcs import get_labels, lil_endian_int, product

import pyphi
import pyphi.compute
from pyphi.labels import NodeLabels

pyphi.config.PARALLEL_CONCEPT_EVALUATION = False
pyphi.config.PARALLEL_CUT_EVALUATION = False
pyphi.config.PARALLEL_COMPLEX_EVALUATION = False
#! Here should be re-implemented/located any routes/metrics.py logic.


class Metric:
    """Class Metrics is used to operate the metrics endpoint required logic."""

    def __init__(
        self,
        istate: str,
        struct: StructureResponse,
        tensor: NDArray[np.float64],
        subsys: str,
        dual: bool,
    ) -> None:
        self.__sup_struct: Structure = Structure(
            db_struct=struct.model_dump(),
            istate=istate,
            tensor=tensor,
        )
        self.__tensor = tensor
        self.__str_bgcond: str = subsys
        self.__dual: bool = dual

    def combine_system(self):
        ic(
            self.__sup_struct,
            self.__tensor,
        )
        bg_set = set(
            idx for idx, bg in enumerate(self.__str_bgcond) if (bg == STR_ONE) == (not self.__dual)
        )

        tensor: OrderedDict = self.__sup_struct.get_tensor()
        tpms = np.array([mat.get_arr()[:, COLS_IDX] for mat in tensor.values()])
        tpm_state_node: NDArray[np.float64] = np.column_stack(tpms)

        num_nodes: int = self.__sup_struct.get_tensor_len()
        istate = tuple(int(i) for i in self.__sup_struct.get_istate())

        str_labels = get_labels(num_nodes)
        idx_labels = tuple(range(num_nodes))
        labels = NodeLabels(str_labels, idx_labels)

        bg_labels: tuple[int] = tuple(
            i for i, bg in enumerate(self.__str_bgcond) if (bg == STR_ONE) == (not self.__dual)
        )

        # ic(bg_labels)

        # future_lbls = bg_labels
        # actual_lbls = tuple(lbl.lower() for lbl in bg_labels)
        size: int = 2
        # complete_nodes = list(tuple(actual_lbls + future_lbls))

        # ic(actual_lbls, future_lbls, complete_nodes)

        """
         ic| list(it.combinations(actual_lbls, size)): [('a', 'b'), ('a', 'c'), ('b', 'c')]
ic| list(it.product(actual_lbls, future_lbls)): [('a', 'A'),
                                                 ('a', 'B'),
                                                 ('a', 'C'),
                                                 ('b', 'A'),
                                                 ('b', 'B'),
                                                 ('b', 'C'),
                                                 ('c', 'A'),
                                                 ('c', 'B'),
                                                 ('c', 'C')]
ic| list(it.combinations(future_lbls, size)): [('A', 'B'), ('A', 'C'), ('B', 'C')]
           """

        self_rel = list(it.combinations(bg_labels, size))
        prod_rel = list(it.product(bg_labels, bg_labels))

        ic(self_rel, prod_rel)
        # actual_actual = list(it.combinations(actual_lbls, size))
        # actual_future = list(it.product(actual_lbls, future_lbls))
        # future_future = list(it.combinations(future_lbls, size))

        network = pyphi.Network(tpm=tpm_state_node, node_labels=labels)

        sub_system = pyphi.Subsystem(
            network=network,
            state=istate,
            nodes=bg_labels,
        )

        # Combinaciones con mismo alcance

        #! Aca se omite el proceso dual

        for mech in self_rel:
            comp_mech = tuple(i for i in bg_labels if i not in set(bg_labels))
            comp_purv = tuple(i for i in bg_labels if i not in set(mech))

            # ? Reconstrucción distribución dual (la primal no tiene sentido)
            # ic(comp_mech, mech, bg_labels, comp_purv)
            dual_er = sub_system.effect_mip(bg_labels, comp_purv)
            # ic(dual_er)

            repertoire = dual_er.repertoire
            repertoire = repertoire.squeeze()

            sub_states: list[tuple[int, ...]] = copy.copy(list(lil_endian_int(repertoire.ndim)))

            distribution: list[float] = [repertoire[sub_state] for sub_state in sub_states]

            # print(f'\n({comp_mech}|{mech})x({bg_labels}|{comp_purv})')
            # ic(distribution)

        # Combinaciones mecanismo y alcance

        #! Aca no se omite nada
        for lbl_prim in bg_labels:
            prim_comp = tuple(lbl for lbl in bg_labels if lbl != lbl_prim)
            for lbl_dual in bg_labels:
                dual_comp = tuple(lbl for lbl in bg_labels if lbl != lbl_dual)

                # print(((lbl_prim,), (lbl_dual,)), 'x', (prim_comp, dual_comp))

                prim_er = sub_system.effect_mip((lbl_prim,), (lbl_dual,))

                repertoire = prim_er.repertoire
                repertoire = repertoire.squeeze()

                sub_states: list[tuple[int, ...]] = copy.copy(list(lil_endian_int(repertoire.ndim)))

                dist_prim: list[float] = [repertoire[sub_state] for sub_state in sub_states]
                idx_dist_prim = (lbl_dual, dist_prim)

                print((lbl_prim,), (lbl_dual,), dist_prim)

                #

                dual_er = sub_system.effect_mip(prim_comp, dual_comp)
                repertoire = dual_er.repertoire
                repertoire = repertoire.squeeze()

                sub_states: list[tuple[int, ...]] = copy.copy(list(lil_endian_int(repertoire.ndim)))

                dist_dual: list[float] = [repertoire[sub_state] for sub_state in sub_states]
                idx_dist_dual = (dual_comp, dist_dual)

                print(prim_comp, dual_comp, dist_dual)
                print()
                subtensor = product(idx_dist_prim, idx_dist_dual)
                # dist_dual

        # Combinaciones con mismo mecanismo
        # primal = list(it.combinations(bg_labels, size))
        for mech in self_rel:
            break
            # (0 1) (1 2) (0 2)
            comp_purv = tuple(i for i in bg_labels if i not in set(mech))
            comp_mech = tuple(i for i in bg_labels if i not in set(bg_labels))

            #! Reconstrucción distribución primal (omision)
            # prim_er = sub_system.effect_mip(mech, comp_purv)
            # # ic(mech, comp_purv)
            # # ic(comp_mech, bg_labels)
            # # ic(bg_labels, mech)

            # repertoire = prim_er.repertoire
            # ic(repertoire)
            # repertoire = repertoire.squeeze()

            # sub_states: list[tuple[int, ...]] = copy.copy(list(lil_endian_int(repertoire.ndim)))

            # distribution: list[float] = [repertoire[sub_state] for sub_state in sub_states]

            # ic(distribution)

            #! Reconstrucción distribución dual
            dual_er = sub_system.effect_mip(comp_purv, bg_labels)
            ic(dual_er)
            print(f'({mech}|{comp_mech})x({comp_purv}|{bg_labels})')

            repertoire = dual_er.repertoire
            repertoire = repertoire.squeeze()

            sub_states: list[tuple[int, ...]] = copy.copy(list(lil_endian_int(repertoire.ndim)))

            distribution: list[float] = [repertoire[sub_state] for sub_state in sub_states]

            ic(distribution)
            # dual_er
