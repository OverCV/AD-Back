from abc import ABC, abstractmethod
from fastapi import HTTPException
import numpy as np
import networkx as nx
from api.models.props.sia import SiaType
from api.models.structure import Structure
from constants.structure import VOID
from utils.consts import CAUSES, DIST, EFFECT, INFTY_POS, INT_ZERO, SUB_DIST, NET_ID, MIP, SMALL_PHI
from numpy.typing import NDArray

from icecream import ic

from utils.funcs import get_labels


class Sia(ABC):
    """Class Sia is used as parent class to use it's props in the used strategies."""

    def __init__(self, structure, effect, causes, distribution, dual) -> None:
        self._structure: Structure = structure
        self._effect: list[int] = effect
        self._causes: list[int] = causes
        self._target_dist: NDArray[np.float64] = distribution
        self._dual: bool = dual

        self.integrated_info: float = None
        self.min_info_part: tuple[tuple[tuple[str], tuple[str]]] = None
        self.sub_distrib: NDArray[np.float64] = None
        # ! Eliminar la id de red [#12] ! #
        self.network_id: nx.Graph | nx.DiGraph = None

    def calculate_concept(self) -> None:
        # Analyze method returns a boolean that indicates if there's NOT a standard parameter solution
        # Obliga a que se deben de asignar los resultados dentro del método analyze, caso contrario se activa la excepción puesto se detecta hay un parámetro sin calcular (faltante).
        if self.analyze():
            raise HTTPException(
                status_code=500,
                detail=f'One or more of the SIA properties are not calculated: {self.integrated_info=}, {self.min_info_part=}, {self.sub_distrib=}, {self.network_id=}',
            )

    def get_reperoire(self) -> dict:
        ic(self.integrated_info, self.min_info_part, self.sub_distrib, self.network_id)
        concept: SiaType = {
            SMALL_PHI: self.integrated_info,
            MIP: self.min_info_part,
            SUB_DIST: self.sub_distrib.tolist(),
            DIST: self._target_dist.tolist(),
            NET_ID: self.network_id,
        }
        return concept

    @abstractmethod
    def analyze(self) -> SiaType:
        pass

    def label_mip(self, partition: tuple[str, str]) -> tuple[tuple[tuple[str], tuple[str]]]:
        # Incrementamos uno puesto son índices de arreglo
        max_len = max(*self._effect, *self._causes) + 1
        labels = get_labels(max_len)
        concepts = [self._effect, self._causes]
        mip = [[[], []], [[], []]]

        for k, (part, con) in enumerate(zip(partition, concepts)):
            ic(k, part, con)
            for b, lbl_idx in zip(part, con):
                mip[int(b)][k].append(labels[lbl_idx])

        for con in mip[EFFECT]:
            if len(con) == INT_ZERO:
                con.append(VOID)
        for con in mip[CAUSES]:
            if len(con) == INT_ZERO:
                con.append(VOID)

        return tuple(mip)
