from copy import deepcopy
from api.models.genetic.individual import Individual


class Population:
    """Class Population is used to cause effects over the individuals."""

    def __init__(self) -> None:
        self._individuals: list[Individual] = []
        self._channels: dict[str, list[str]] = None
        # self._subtensor: list[Matrix] = list()

    def get_size(self) -> int:
        return len(self._individuals)

    def get_individuals(self) -> list[Individual]:
        return deepcopy(self._individuals)

    def set_individuals(self, individuals: list[Individual]) -> None:
        self._individuals = individuals

    def set_channels(self, channels: dict[str, list]) -> None:
        self._channels = channels

    # def set_subtensor(self, sub_tensor: list[Matrix]) -> None:
    #     self._subtensor = sub_tensor

    # def get_subtensor(self) -> list[Matrix]:
    #     return deepcopy(self._subtensor)

    def generate_individuals(self, pop_size, channels) -> None:
        """
        INPUT -> ABC|DE: cms1 = [011.01]
                                (BC.E)(A.D)
        """
