import numpy as np
from numpy.typing import NDArray


class Deletion:
    """Class Deletion (Record?) is used in the iterative phase to know the actual graph state."""

    def __init__(
        self,
        edge: tuple[int, int] = 0.0,
        omega: list[tuple[int, int]] = 0.0,
        minuend_emd: float = 0.0,
        subtrahend_emd: float = 0.0,
        emd: float = 0.0,
        disconnected: bool = False,
        subdist: NDArray[np.float64] | None = None,
    ) -> None:
        """

        Args:

        """
        self.__edge: tuple[int, int] = edge
        self.__omega: list[tuple[int, int]] = omega
        self.__minuend_emd: float = minuend_emd
        self.__subtrahend_emd: float = subtrahend_emd
        self.__emd: float = emd
        self.__disconnected: bool = disconnected
        self.__subdist: NDArray[np.float64] | None = subdist

    def get_edge(self) -> tuple[int, int]:
        return self.__edge

    def get_omega(self) -> list[tuple[int, int]]:
        return self.__omega

    def get_emd(self) -> float:
        return self.__emd

    def get_minuend_emd(self) -> float:
        return self.__minuend_emd

    def get_subtrahend_emd(self) -> float:
        return self.__subtrahend_emd

    def is_disconn(self) -> bool:
        return self.__disconnected

    def get_subdist(self) -> NDArray[np.float64] | None:
        return self.__subdist

    def __str__(self) -> str:
        return f'Deletion: {self.__omega} ∪ [{self.__edge}] | {self.__minuend_emd:.2f} - {self.__subtrahend_emd:.2f} = {self.__emd:.2f}{' - B' if self.__disconnected else ''}'
