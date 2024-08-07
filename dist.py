import numpy as np
from pyemd import emd
from decimal import Decimal, getcontext  # Esto es para lograr mayor precision en los calculos

# Set the precision to 50 decimal places
getcontext().prec = 50





# Ejemplo
p = [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]  # Distribución de probabilidades 1
q = [0.0, 0.0, 0.0, 0.0, 0.38, 0.38, 0.13, 0.13]  # Distribución de probabilidades 2

emd_value = emd_hamming(p, q)
print(f'EMD using Hamming distance: {emd_value}')
