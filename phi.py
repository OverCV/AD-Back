# Obtenemos el arreglo desde el archivo .csv

import numpy as np
import pandas as pd

from numpy.typing import NDArray

# Leer el archivo CSV
df = pd.read_csv(
    'assets/tpm_n2s/tpm_fly1_awake_lil_endian.csv',
    header=None,
)

# Convertir el DataFrame en un numpy array
arr: NDArray[np.float64] = np.vstack(
    df[0].apply(
        lambda x: np.fromstring(x.strip('[]'), sep=','),
    )
)


print(arr.shape)
