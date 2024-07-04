CROSS_RATE: str = 'xi'
INIT_POP_SIZE: str = 'r'
MUTATE_RATE: str = 'mu'
MAX_GENS: str = 'G'

DECAY: str = 'decay'
PARENTS_NUM: str = 'parents_num'
CROSSED_IND: str = 'crossed_ind'
MAX_STREAK: str = 'max_streak'


DEFAULT_PARAMS: dict[str, float | int] = {
    INIT_POP_SIZE: 60,
    CROSS_RATE: 0.6,
    MUTATE_RATE: 0.1,
    MAX_GENS: 100,
    #
    DECAY: 10,
    PARENTS_NUM: 2,
    CROSSED_IND: 2,
    MAX_STREAK: 3,
}
