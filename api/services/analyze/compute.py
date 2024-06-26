from re import S
import numpy as np
from fastapi import HTTPException
from api.models.mechanism import Mechanism
from api.schemas.system import SystemResponse

from numpy.typing import NDArray

from api.shared.validators import analyze as av
from api.services.analyze.strats.genetic import Genetic
from api.services.analyze.strats.force import BruteForce


class Compute:
    ''' Class Compute is used to compute all different System Irreducibility analysis. '''

    def __init__(
        self,
        system: SystemResponse,
        istate: str,
        effect: str,
        causes: str,
        subtensor: list[NDArray[np.float64]]
    ) -> None:
        self.__effect: str = effect
        self.__causes: str = causes
        self.__supsystem: Mechanism = Mechanism(
            db_sys=system.model_dump(),
            istate=istate,
            tensor=subtensor,
        )

    def use_brute_force(self) -> bool:
        sia_force = BruteForce()
        sia_force.calculate_repertoire()
        return sia_force.get_reperoire()

    def use_genetic_algorithm(self) -> bool:
        if not av.has_valid_inputs(
            len(self.__supsystem.get_istate()),
            len(self.__effect),
            len(self.__causes),
            len(self.__supsystem.get_tensor())
        ):
            raise HTTPException(
                status_code=400,
                detail='Invalid effect, causes or istate.'
            )
        # ! Made for S2P
        # Seteamos los estados futuros y presentes
        self.__supsystem.set_effect(self.__effect)
        self.__supsystem.set_causes(self.__causes)

        system = self.__supsystem
        # system.subsystem()
        system.correlate()
        system.calculate_dist()

        sia_genetic: Genetic = Genetic(system)
        sia_genetic.calculate_repertoire()
        return sia_genetic.get_reperoire()
        # ! Dada una cadena de binarios y una lista de elementos, las combinaciones binarias de elementos determinan si el elemento se va al True o al False de los canales del efecto o causa que se maneje

        # if not sv.has_valid_istate(system.istate, len(subtensor)):
        #     raise HTTPException(
        #         status_code=status.HTTP_400_BAD_REQUEST,
        #         detail=f'Invalid initial state: State {
        #             system.istate} needs to be size {len(subtensor)}.'
        #     )

    def use_pyphi(self) -> bool:
        pass

    def use_brute_force(self) -> bool:
        sia_force = BruteForce()
        sia_force.calculate_repertoire()
        return sia_force.get_reperoire()

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
