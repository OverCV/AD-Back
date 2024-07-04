from api.models.genetic.individual import Individual


class Reporter:
    """Class Log is used to report statistics of the genetic algorithm."""

    def __init__(self) -> None:
        self._bests_inds: list[Individual] = list()
        # self._num_generations: list[int] = [0]

    def get_best_individual(self) -> Individual:
        if self._bests_inds == list():
            return None
        return min(self._bests_inds, key=lambda ind: ind.get_fit())

    def get_bests_individuals(self) -> list[Individual]:
        return self._bests_inds
