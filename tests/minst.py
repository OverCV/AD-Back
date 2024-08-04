import networkx as nx
import matplotlib.pyplot as plt
from pandas import cut

# Crear un grafo con pesos en las aristas
G = nx.Graph()
# edges = [
#     ('A(0)', 'A(1)', 0.5),
#     ('B(0)', 'A(1)', 0.9),
#     ('C(0)', 'A(1)', 0.4),
#     ('A(0)', 'B(1)', 0.3),
#     ('B(0)', 'B(1)', 0.8),
#     ('C(0)', 'B(1)', 0.45),
#     ('A(0)', 'C(1)', 0.6),
#     ('B(0)', 'C(1)', 0.7),
#     ('C(0)', 'C(1)', 0.2),
# ]

G.add_weighted_edges_from(edges)

# Obtener el minimum cut mediante el algoritmo de Stoer-Wagner
cut_value, partition = nx.stoer_wagner(G)

print(cut_value, partition)

# Dibujar el grafo original
pos = nx.spring_layout(G)
plt.figure(figsize=(10, 5))

plt.subplot(121)
nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray')
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.title('Grafo Original')

# Dibujar el corte mínimo
plt.subplot(122)
nx.draw(G, pos, with_labels=True, node_color='lightgreen', edge_color='red')
nx.draw_networkx_nodes(G, pos, nodelist=partition[0], node_color='lightblue')
nx.draw_networkx_nodes(G, pos, nodelist=partition[1], node_color='lightgreen')
nx.draw_networkx_edges(G, pos)
plt.title('Corte Mínimo')

plt.show()


# # Obtener el MST usando el algoritmo de Kruskal
# mst = nx.minimum_spanning_tree(G, algorithm='kruskal')

# # Dibujar el grafo original
# pos = nx.spring_layout(G)
# plt.figure(figsize=(10, 5))

# plt.subplot(121)
# nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray')
# labels = nx.get_edge_attributes(G, 'weight')
# nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
# plt.title('Grafo Original')

# # Dibujar el MST
# plt.subplot(122)
# nx.draw(mst, pos, with_labels=True, node_color='lightgreen', edge_color='red')
# labels_mst = nx.get_edge_attributes(mst, 'weight')
# nx.draw_networkx_edge_labels(mst, pos, edge_labels=labels_mst)
# plt.title('Árbol de Expansión Mínima (MST)')

# plt.show()
