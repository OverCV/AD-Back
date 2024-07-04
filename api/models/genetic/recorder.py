from api.models.genetic.individual import Individual


class Recorder:
    """Class Log is used to report statistics of the genetic algorithm."""

    def __init__(self) -> None:
        self.__bests_inds: list[Individual] = list()
        # self._num_generations: list[int] = [0]

    def add_best_individual(self, ind: Individual) -> None:
        self.__bests_inds.append(ind)

    def get_best_individual(self) -> Individual:
        if self.__bests_inds == list():
            return None
        return min(self.__bests_inds, key=lambda ind: ind.get_fit())

    def get_bests_individuals(self) -> list[Individual]:
        return self.__bests_inds


rec = Recorder()
