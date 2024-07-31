import networkx as nx
import matplotlib.pyplot as plt

# Crear un grafo bipartito
B = nx.Graph()

# Número de nodos en cada conjunto
num_nodes = 4

# Añadir nodos a los conjuntos U y V
U = [f'u{i+1}' for i in range(num_nodes)]
V = [f'v{i+1}' for i in range(num_nodes)]

# Añadir los nodos al grafo
B.add_nodes_from(U, bipartite=0)
B.add_nodes_from(V, bipartite=1)

# Conectar cada nodo de U con cada nodo de V
edges = [(u, v) for u in U for v in V]
B.add_edges_from(edges)

# Crear un layout circular intercalado para los nodos
# Primero creamos una lista intercalada de nodos
intercalado = [None] * (len(U) + len(V))
intercalado[::2] = U
intercalado[1::2] = V

# Crear un layout circular para los nodos intercalados
pos = nx.circular_layout(intercalado)

# Dibujar el grafo
plt.figure(figsize=(8, 8))
nx.draw(B, pos, with_labels=True, node_color='lightblue', edge_color='gray')
plt.title('Grafo Bipartito en Forma de Caparazón')
plt.show()
