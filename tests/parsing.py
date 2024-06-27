import timeit


# Método con map y lambda
setup_map = "chain = '100101'"
stmt_map = "list(map(lambda x: x == '1', chain))"


# Método con list comprehension
setup_lc = "chain = '100101'"
stmt_lc = "[c == '1' for c in chain]"

# Método con NumPy
setup_np = "import numpy as np; chain = '100101'"
stmt_np = "np.array(list(chain)) == '1'"

# Tiempos de ejecución
print('Map y Lambda:', timeit.timeit(stmt=stmt_map, setup=setup_map, number=10000))
print('List Comprehension:', timeit.timeit(stmt=stmt_lc, setup=setup_lc, number=10000))
print('NumPy:', timeit.timeit(stmt=stmt_np, setup=setup_np, number=10000))

print('Map y Lambda:', timeit.timeit(stmt=stmt_map, setup=setup_map, number=10000))
print('List Comprehension:', timeit.timeit(stmt=stmt_lc, setup=setup_lc, number=10000))
print('NumPy:', timeit.timeit(stmt=stmt_np, setup=setup_np, number=10000))
