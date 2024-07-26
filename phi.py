import pyphi
from pyphi.labels import NodeLabels
from pyphi.models import RepertoireIrreducibilityAnalysis

import numpy as np
import pandas as pd

from numpy.typing import NDArray

from utils.consts import COLS_IDX
from utils.funcs import get_labels

# path = 'assets/tpm_n2s/tpm_fly1_awake_lil_endian.csv'
path = 'assets/tpm_n2s/F5.xlsx'

# CSV Con 15 nodos
# df = pd.read_csv(path, header=None)

# # Convertir el DataFrame en un numpy array
# arr: NDArray[np.float64] = np.vstack(
#     df[0].apply(
#         lambda x: np.fromstring(x.strip('[]'), sep=','),
#     )
# )

arr: NDArray[np.float64] = pd.read_excel(path, header=None).to_numpy(dtype=np.float64)
num_nodes = arr.shape[COLS_IDX]

print(arr)

str_nodes = get_labels(num_nodes)
idx_nodes = tuple(range(num_nodes))
labels = NodeLabels(str_nodes, idx_nodes)

print(str_nodes, idx_nodes, labels)


net = pyphi.Network(
    tpm=arr,
    node_labels=labels,
)

net = pyphi.examples.fig4()

# str_bg = ('A', 'B', 'C', 'D', 'E')
str_bg = ('A', 'B', 'C')

for idx in range(2**num_nodes):
    str_istate = f'{idx:0{num_nodes}b}'
    istate = tuple(map(int, str_istate))
    print(istate)
    subsys = pyphi.Subsystem(
        network=net,
        state=istate,
        nodes=str_bg,
    )
    print(subsys)

    # er: RepertoireIrreducibilityAnalysis = subsys.effect_repertoire(
    #     mechanism='full',
    #     direction='past',
    # )
