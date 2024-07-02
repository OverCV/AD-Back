import networkx as nx
import itertools
from pytest import Session
from api.schemas.network.schema import NetworkSchema

from icecream import ic

from constants.structure import VOID
from utils.consts import BASE_2, CAUSES, COLS_IDX, EFFECT, ROWS_IDX

# ! Debería haber un decorador, puesto para almacenar la mip debe pode existir el endpoint que haga la llamada al otro endpoint con el servicio para redes [#10] ! #
# async def stablish_connection(db: Session) -> None:
#     # async def create_network(network: NetworkSchema = Body(...)):
#     try:
#         db = await get_mongo()
#         # reconstruct_network(network, db)
#         # new_network: any = await db.insert_one(
#         #     network.model_dump(by_alias=True, exclude=['id'])
#         # )
#         stored_network = await db.find_one({'_id': new_network.inserted_id})
#         return JSONResponse(
#             status_code=status.HTTP_201_CREATED,
#             content={DATA: jsonable_encoder(
#                 NetworkSchema(**stored_network)
#             )}
#         )
#     except ServerSelectionTimeoutError:
#         print('Error connecting to remote MongoDB, falling back to local MongoDB.')
#         conf.use_locale_nosql()
#         db = await get_mongo()

#         new_network: any = await db.insert_one(
#             network.model_dump(by_alias=True, exclude=['id'])
#         )
#         stored_network = await db.find_one({'_id': new_network.inserted_id})
#         return JSONResponse(
#             status_code=status.HTTP_201_CREATED,
#             content={DATA: jsonable_encoder(
#                 NetworkSchema(**stored_network)
#             )}
#         )
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))


def reconstruct_network(mip: tuple[tuple[tuple[str], tuple[str]]], db: Session) -> NetworkSchema:
    """Designer for bipartite graphs"""
    ic()
    ic(mip)

    # ic| mip: ([['A', 'B', 'D'], ['∅']], [['∅'], ['B', 'D', 'E']])
    nodes = set()

    prim = mip[ROWS_IDX]
    dual = mip[COLS_IDX]
    # Creación de los nodos
    nodes = [
        []
        if prim[EFFECT] == [VOID]
        else [{'name': x + 'f', 'type': 'effect'} for x in prim[EFFECT]],
        []
        if prim[CAUSES] == [VOID]
        else [{'name': x + 'c', 'type': 'cause'} for x in prim[CAUSES]],
        []
        if dual[EFFECT] == [VOID]
        else [{'name': y + 'f', 'type': 'effect'} for y in dual[EFFECT]],
        []
        if dual[CAUSES] == [VOID]
        else [{'name': y + 'c', 'type': 'cause'} for y in dual[CAUSES]],
    ]

    # Flatten the list and discard VOID nodes
    nodes = [node for sublist in nodes for node in sublist]
    nodes = [node for node in nodes if node['name'] != VOID]

    ic(nodes)

    prim_edges = list(
        itertools.product(
            [] if prim[COLS_IDX] == [VOID] else [x + 'c' for x in prim[COLS_IDX]],
            [] if prim[ROWS_IDX] == [VOID] else [x + 'f' for x in prim[ROWS_IDX]],
        )
    )
    # dual_edges = list(itertools.product(dual[COLS_IDX], dual[ROWS_IDX]))
    dual_edges = list(
        itertools.product(
            [] if dual[COLS_IDX] == [VOID] else [x + 'c' for x in dual[COLS_IDX]],
            [] if dual[ROWS_IDX] == [VOID] else [y + 'f' for y in dual[ROWS_IDX]],
        )
    )
    ic(prim_edges, dual_edges)

    # Crear un grafo dirigido
    G = nx.DiGraph()

    # Añadir vértices
    # G.add_nodes_from(nodes)

    for node in nodes:
        G.add_node(node['name'], **node)
    # Añadir aristas
    G.add_edges_from(prim_edges)
    G.add_edges_from(dual_edges)

    # Imprimir el grafo para verificar

    ic(G.nodes)
    ic(G.edges)

    vertices = set()
    for node in G.nodes(data=True):
        ic(node)

    arcs = set()
    for u, v, data in G.edges(data=True):
        ic(u, v, data)
        # vertices.add(node)

    # Opcional: Dibujar el grafo para visualizarlo
    # import matplotlib.pyplot as plt

    # pos = nx.spring_layout(G)  # Posiciones de los nodos para la visualización
    # nx.draw(G, pos, with_labels=True, node_size=700, node_color='skyblue', arrowsize=20)
    # plt.show()

    # for effect, cause in mip:
    #     ic(effect, cause)
    # vertices.update(effect)
    # vertices.update(cause)

    # network = NetworkTable()
    # db.add(network)
    # db.commit()
    # db.refresh(network)
    # return network
