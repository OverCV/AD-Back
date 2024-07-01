from typing import Callable, OrderedDict
import numpy as np
from fastapi import HTTPException
from sqlalchemy.orm import Session
from api.models.props.structure import StructProps
from api.models.structure import Structure
from api.schemas.structure import StructureResponse

from numpy.typing import NDArray

from api.shared.validators import analyze as av
from api.services.analyze.strats.genetic import Genetic
from api.services.analyze.strats.force import BruteForce
from constants.structure import BOOL_RANGE
from utils.consts import COLS_IDX, ROWS_IDX, STR_ONE, STR_ZERO

from icecream import ic
from copy import copy
from server import conf


class Compute:
    """Class Compute is used to compute all different System Irreducibility analysis."""

    def __init__(
        self,
        struct: StructureResponse,
        istate: str,
        effect: str,
        causes: str,
        subtensor: NDArray[np.float64],
        dual: bool = False,
    ) -> None:
        # Siempre preservamos la superestructura
        self.__sup_struct: Structure = Structure(
            db_struct=struct.model_dump(),
            istate=istate,
            tensor=subtensor,
        )
        self.__effect: str = effect
        self.__causes: str = causes
        self.__dual: bool = dual

    # def use_pyphi(self) -> bool:
    #     pass

    def use_brute_force(self) -> bool:
        effect = {False: [], True: []}
        causes = {False: [], True: []}
        for i, e in enumerate(self.__effect):
            effect[e == STR_ONE].append(i)
        for j, c in enumerate(self.__causes):
            causes[c == STR_ONE].append(j)
        # Preservamos la superestructura para trabajar con una nueva
        struct: Structure = copy(self.__sup_struct)
        struct.create_concept(effect, causes)
        distrib = struct.get_distribution(self.__dual)
        ic(distrib)

        # raise HTTPException(status_code=400, detail='TESTING STOP.')

        sia_force: BruteForce = BruteForce(
            struct,
            effect[not self.__dual],
            causes[not self.__dual],
            distrib,
            self.__dual,
        )
        sia_force.calculate_concept()
        return sia_force.get_reperoire()

    def use_genetic_algorithm(self, db: Session) -> bool:
        # ! Made for S2P

        # Definimos los concepto causa y efecto
        effect = {False: [], True: []}
        causes = {False: [], True: []}
        for i, e in enumerate(self.__effect):
            effect[e == STR_ONE].append(i)
        for j, c in enumerate(self.__causes):
            causes[c == STR_ONE].append(j)
        ic(effect, causes)
        # New strcuture with original tensor
        struct: Structure = copy(self.__sup_struct)
        # raise HTTPException(status_code=400, detail='TESTING STOP.')
        struct.create_concept(effect, causes)
        distrib = struct.get_distribution(self.__dual)
        # From this superior level we have control of the EC structure.
        # Obtenemos la distribución que indique el usuario
        ic(effect, causes)
        ic(distrib)
        sub_tensor: OrderedDict = OrderedDict(
            # Si estamos con le primal o dual, tomamos dichos futuros como, dichas matrices del tensor original
            (k, struct.get_tensor()[k])
            for k in effect[not self.__dual]
        )
        ic(sub_tensor)
        # La subestructura no tiene efecto ni causa, esto puesto aún no está particionada
        sub_struct: Structure = Structure(
            db_struct={
                StructProps.TITLE: f'Sub-Struct {struct.get_title()}',
                # StructProps.SIZE: sum(len(effect[b]) for b in BOOL_RANGE),
            },
            istate=struct.get_istate(),
            tensor=sub_tensor,
        )
        sia_genetic: Genetic = Genetic(
            sub_struct, effect[not self.__dual], causes[not self.__dual], distrib, self.__dual
        )

        # [ic(k, m.as_dataframe()) for k, m in struct.get_tensor().items()]

        sia_genetic.calculate_concept()
        return sia_genetic.get_reperoire()
        # ! Dada una cadena de binarios y una lista de elementos, las combinaciones binarias de elementos determinan si el elemento se va al True o al False de los canales del efecto o causa que se maneje

        # if not sv.has_valid_istate(system.istate, len(subtensor)):
        #     raise HTTPException(
        #         status_code=status.HTTP_400_BAD_REQUEST,
        #         detail=f'Invalid initial state: State {
        #             system.istate} needs to be size {len(subtensor)}.'
        #     )

    def use_branch_and_bound(self) -> bool:
        pass

    def use_dynamic_programming(self) -> bool:
        pass

    def use_game_theory(self) -> bool:
        pass

    def use_evolutionary_algorithm(self) -> bool:
        pass

    def use_differential_evolution(self) -> bool:
        pass

    def use_simulated_annealing(self) -> bool:
        pass

    def use_tabu_search(self) -> bool:
        pass

    def use_stochastic_programming(self) -> bool:
        pass

    def use_ant_colony(self) -> bool:
        pass

    def use_swarm_intelligence(self) -> bool:
        pass

    def use_neural_network(self) -> bool:
        pass

    def use_deep_learning(self) -> bool:
        pass

    def use_markov_decision_process(self) -> bool:
        pass

    def use_hidden_markov_model(self) -> bool:
        pass

    def use_reinforcement_learning(self) -> bool:
        pass

    def use_linear_programming(self) -> bool:
        pass

    def use_integer_programming(self) -> bool:
        pass

    def use_convex_optimization(self) -> bool:
        pass

    def use_nonlinear_programming(self) -> bool:
        pass

    def use_quadratic_programming(self) -> bool:
        pass

    def use_semi_definite_programming(self) -> bool:
        pass

    def use_boolean_programming(self) -> bool:
        pass

    def use_fuzzy_programming(self) -> bool:
        pass

    def use_quantum_neural_network(self) -> bool:
        pass

    def use_wave_function_collapse(self) -> bool:
        pass

    def use_backpropagation(self) -> bool:
        pass

    def use_convolutional_neural_network(self) -> bool:
        pass

    def use_q_learning(self) -> bool:
        pass

    def use_deep_q_learning(self) -> bool:
        pass

    def use_policy_gradient(self) -> bool:
        pass

    def use_actor_critic(self) -> bool:
        pass

    def use_multi_objective_programming(self) -> bool:
        pass

    def use_decision_theory(self) -> bool:
        pass

    def use_markov_chain(self) -> bool:
        pass

    def use_markov_random_field(self) -> bool:
        pass

    def use_bayesian_network(self) -> bool:
        pass

    def use_belief_propagation(self) -> bool:
        pass

    """  """

    def use_gibbs_sampling(self) -> bool:
        pass

    def use_variational_inference(self) -> bool:
        pass

    def use_expectation_maximization(self) -> bool:
        pass

    def use_kalman_filter(self) -> bool:
        pass

    def use_particle_filter(self) -> bool:
        pass

    def use_ensemble_filter(self) -> bool:
        pass

    def use_extended_kalman_filter(self) -> bool:
        pass

    def use_unscented_kalman_filter(self) -> bool:
        pass

    def use_information_filter(self) -> bool:
        pass

    def use_smoothed_particle_filter(self) -> bool:
        pass

    def use_rao_blackwellized_particle_filter(self) -> bool:
        pass

    def use_gaussian_filter(self) -> bool:
        pass

    def use_extended_information_filter(self) -> bool:
        pass

    def use_unscented_information_filter(self) -> bool:
        pass

    def use_extended_gaussian_filter(self) -> bool:
        pass

    def use_unscented_gaussian_filter(self) -> bool:
        pass

    def use_finite_state_machine(self) -> bool:
        pass

    def use_turing_machine(self) -> bool:
        pass

    def use_neural_turing_machine(self) -> bool:
        pass

    def use_recurrent_neural_network(self) -> bool:
        pass

    def use_long_short_term_memory(self) -> bool:
        pass

    def use_gated_recurrent_unit(self) -> bool:
        pass

    def use_bidirectional_recurrent_neural_network(self) -> bool:
        pass

    def use_deep_belief_network(self) -> bool:
        pass

    def use_restricted_boltzmann_machine(self) -> bool:
        pass

    def use_autoencoder(self) -> bool:
        pass

    def use_multi_layer_perceptron(self) -> bool:
        pass

    def use_radial_basis_function_network(self) -> bool:
        pass

    def use_optical_neural_network(self) -> bool:
        pass

    def use_pulsed_neural_network(self) -> bool:
        pass

    def use_spiking_neural_network(self) -> bool:
        pass

    def use_neuromorphic_engineering(self) -> bool:
        pass

    def use_neural_network_quantum_state(self) -> bool:
        pass

    def use_hopfield_network(self) -> bool:
        pass

    def use_associative_memory(self) -> bool:
        pass

    def use_widrow_hoff_rule(self) -> bool:
        pass

    def use_resilient_backpropagation(self) -> bool:
        pass

    def use_quickprop(self) -> bool:
        pass

    def use_contrastive_divergence(self) -> bool:
        pass

    def use_stochastic_gradient_descent(self) -> bool:
        pass

    def use_batch_gradient_descent(self) -> bool:
        pass

    def use_yarowsky_algorithm(self) -> bool:
        pass

    def use_zhang_shasha_algorithm(self) -> bool:
        pass

    def use_hungarian_algorithm(self) -> bool:
        pass
