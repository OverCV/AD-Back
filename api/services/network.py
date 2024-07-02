import networkx as nx
import itertools
from pytest import Session
from api.models.props.network import DataProps, VertexProps
from api.schemas.network.schema import NetworkSchema

from api.models.props import spectrum

from constants.structure import VOID
from utils.color import get_rnd_colors
from utils.consts import BASE_2, CAUSES, COLS_IDX, EFFECT, ROWS_IDX

from matplotlib import pyplot as plt
from icecream import ic
# ! Debería haber un decorador para stablish_connection, puesto para almacenar la mip debe pode existir el endpoint que haga la llamada al otro endpoint con el servicio para redes [#10] ! #
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
    ic(mip)
    # ic| mip: ([['A', 'B', 'D'], ['∅']], [['∅'], ['B', 'D', 'E']])
    prim_effect = [] if mip[ROWS_IDX][EFFECT] == [VOID] else mip[ROWS_IDX][EFFECT]
    prim_causes = [] if mip[ROWS_IDX][CAUSES] == [VOID] else mip[ROWS_IDX][CAUSES]
    dual_effect = [] if mip[COLS_IDX][EFFECT] == [VOID] else mip[COLS_IDX][EFFECT]
    dual_causes = [] if mip[COLS_IDX][CAUSES] == [VOID] else mip[COLS_IDX][CAUSES]
    # Creación de los nodos
    n_colors = get_rnd_colors(BASE_2, spectrum.FormatProp.HEX)
    e_colors = get_rnd_colors(BASE_2, spectrum.FormatProp.HEX)
    # ic(n_colors,e_colors)
    nodes = [
        [
            {DataProps.LBL: x + 'f', DataProps.COLOR: n_colors[ROWS_IDX], DataProps.value: 0}
            for x in prim_effect
        ],
        [
            {DataProps.LBL: x + 'c', DataProps.COLOR: n_colors[ROWS_IDX], DataProps.value: 0}
            for x in prim_causes
        ],
        [
            {DataProps.LBL: y + 'f', DataProps.COLOR: n_colors[COLS_IDX], DataProps.value: 0}
            for y in dual_effect
        ],
        [
            {DataProps.LBL: y + 'c', DataProps.COLOR: n_colors[COLS_IDX], DataProps.value: 0}
            for y in dual_causes
        ],
    ]
    # Flatten the list
    nodes = [node for sublist in nodes for node in sublist]

    ic(nodes)

    used_prim_edges = list(
        itertools.product(
            [x + 'c' for x in prim_causes],
            [x + 'f' for x in prim_effect],
        )
    )
    used_dual_edges = list(
        itertools.product(
            [x + 'c' for x in dual_causes],
            [y + 'f' for y in dual_effect],
        )
    )
    cutted_edges = list(
        itertools.product(
            [x + 'c' for x in dual_causes],
            [y + 'f' for y in prim_effect],
        )
    ) + list(
        itertools.product(
            [x + 'c' for x in prim_causes],
            [y + 'f' for y in dual_effect],
        )
    )

    ic(used_prim_edges, used_dual_edges, cutted_edges)

    # Crear un grafo dirigido
    G = nx.DiGraph()

    # Añadir vértices
    for node in nodes:
        G.add_node(node[DataProps.LBL], **node)

    # Añadir aristas
    G.add_edges_from(used_prim_edges)
    G.add_edges_from(used_dual_edges)
    G.add_edges_from(cutted_edges)

    # Imprimir el grafo para verificar

    ic(G.nodes)
    ic(G.edges)

    # vertices = set()
    # for node in G.nodes(data=True):
    #     ic(node)

    # arcs = set()
    # for u, v, data in G.edges(data=True):
    #     ic(u, v, data)
    # vertices.add(node)

    # Opcional: Dibujar el grafo para visualizarlo

    pos = nx.shell_layout(G)  # Posiciones de los nodos para la visualización
    nx.draw(G, pos, with_labels=True, node_size=700, node_color='skyblue', arrowsize=20)
    plt.show()

    # for effect, cause in mip:
    #     ic(effect, cause)
    # vertices.update(effect)
    # vertices.update(cause)

    # network = NetworkTable()
    # db.add(network)
    # db.commit()
    # db.refresh(network)
    # return network
