from fastapi import HTTPException
import networkx as nx
import itertools
from numpy import iterable
from pytest import Session
from api.models.props import network as nk
from api.schemas.network.arc import Arc
from api.schemas.network.schema import NetworkSchema

from api.models.props import spectrum

from api.schemas.network.vertex import Vertex
from constants.structure import VOID
from utils.color import get_rnd_colors
from utils.consts import BASE_2, ACTUAL, COLS_IDX, EFFECT, FLOAT_ONE, FLOAT_ZERO, INT_ONE, ROWS_IDX

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


def reconstruct_network(
    mip: tuple[tuple[tuple[str], tuple[str]]], db: Session, axis: int = ROWS_IDX
) -> NetworkSchema:
    """Designer for bipartite graphs"""

    prim_effect = (
        [] if mip[ROWS_IDX][EFFECT] == [VOID] else [x + '(1)' for x in mip[ROWS_IDX][EFFECT]]
    )
    prim_causes = (
        [] if mip[ROWS_IDX][ACTUAL] == [VOID] else [x + '(0)' for x in mip[ROWS_IDX][ACTUAL]]
    )
    dual_effect = (
        [] if mip[COLS_IDX][EFFECT] == [VOID] else [x + '(1)' for x in mip[COLS_IDX][EFFECT]]
    )
    dual_causes = (
        [] if mip[COLS_IDX][ACTUAL] == [VOID] else [x + '(0)' for x in mip[COLS_IDX][ACTUAL]]
    )

    # ic(mip)
    # ic| mip: ([['A', 'B', 'D'], ['∅']], [['∅'], ['B', 'D', 'E']])

    # Creación de los nodos
    vertices: list[Vertex] = reconstruct_nodes(
        [prim_effect, prim_causes], [dual_effect, dual_causes]
    )

    # ic(vertices)

    return
    raise HTTPException(status_code=500, detail='STOP NOW')

    # arcs: list[Arc] = reconstruct_edges(mip)

    # e_colors = get_rnd_colors(BASE_2, spectrum.FormatProp.HEX)
    # # ic(n_colors,e_colors)

    # ic(nodes)

    # used_prim_edges = list(itertools.product(prim_causes, prim_effect))
    # used_dual_edges = list(itertools.product(dual_causes, dual_effect))
    # cutted_edges = list(
    #     itertools.product(dual_causes, prim_effect),
    # ) + list(itertools.product(prim_causes, dual_effect))

    # ic(used_prim_edges, used_dual_edges, cutted_edges)

    # # Creación de esquema

    # vertices = [
    #     Vertex(
    #         id=node[nk.VertexDataProps.LBL],
    #         data=node,
    #         position={'x': prim_x_pos, 'y': prim_y_pos},
    #         type='custom',
    #     )
    #     for node in nodes
    # ]

    # arcs_dual = [
    #     Arc(
    #         id=f'{ude[0]}-{ude[1]}',
    #         source=ude[0],
    #         target=ude[1],
    #         data={
    #             nk.ArcDataProps.COLOR: e_colors[0],
    #             nk.ArcDataProps.WEIGHT: -1,
    #         },
    #         animated=True,
    #     )
    #     for ude in used_dual_edges
    # ]
    # arcs_prim = [
    #     Arc(
    #         id=f'{ude[0]}-{ude[1]}',
    #         source=ude[0],
    #         target=ude[1],
    #         data={
    #             nk.ArcDataProps.COLOR: e_colors[1],
    #             nk.ArcDataProps.WEIGHT: -1,
    #         },
    #         animated=True,
    #     )
    #     for ude in used_prim_edges
    # ]
    # arcs_dual = [
    #     Arc(
    #         id=f'{ude[0]}-{ude[1]}',
    #         source=ude[0],
    #         target=ude[1],
    #         data={
    #             nk.ArcDataProps.COLOR: e_colors[0],
    #             nk.ArcDataProps.WEIGHT: -1,
    #         },
    #         animated=True,
    #     )
    #     for ude in used_dual_edges
    # ]

    # # Crear un grafo dirigido
    # G = nx.DiGraph()

    # # Añadir vértices
    # for node in nodes:
    #     G.add_node(node[nk.VertexDataProps.LBL], **node)

    # # Añadir aristas
    # G.add_edges_from(used_prim_edges)
    # G.add_edges_from(used_dual_edges)
    # G.add_edges_from(cutted_edges)

    # # Imprimir el grafo para verificar

    # ic(G.nodes)
    # ic(G.edges)

    # vertices = set()
    # for node in G.nodes(data=True):
    #     ic(node)

    # arcs = set()
    # for u, v, data in G.edges(data=True):
    #     ic(u, v, data)
    # vertices.add(node)

    # Opcional: Dibujar el grafo para visualizarlo

    # pos = nx.shell_layout(G)  # Posiciones de los nodos para la visualización
    # ic(pos)
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


def reconstruct_nodes(
    prim: tuple[list[str], list[str]], dual: tuple[list[str], list[str]], axis: int = ROWS_IDX
) -> list[Vertex]:
    n_colors = get_rnd_colors(BASE_2, spectrum.FormatProp.HEX)

    # Definir las posiciones iniciales y las diferencias para iterar sobre los nodos
    FLOAT_TEN = FLOAT_ONE * 10
    NODES_GAP: float = FLOAT_TEN
    prim_x_pos: float = NODES_GAP if axis == ROWS_IDX else FLOAT_ZERO
    prim_y_pos: float = FLOAT_ZERO if axis == ROWS_IDX else NODES_GAP

    dual_x_pos: float = FLOAT_ZERO
    dual_y_pos: float = FLOAT_ZERO

    # Iteradores para las posiciones
    iter_prim = enumerate(prim[EFFECT] + prim[ACTUAL])
    iter_dual = enumerate(dual[EFFECT] + dual[ACTUAL])

    nodes = []

    # Añadir nodos duales
    for i, d in iter_dual:
        pos_x = dual_x_pos if axis == ROWS_IDX else NODES_GAP * (i + 1)
        pos_y = NODES_GAP * (i + 1) if axis == ROWS_IDX else dual_y_pos
        node = Vertex(
            id=d,
            data={
                nk.VertexDataProps.LBL: d,
                nk.VertexDataProps.COLOR: n_colors[COLS_IDX],
                nk.VertexDataProps.VALUE: 0,
            },
            position={
                nk.VertexPosProps.X: pos_x,
                nk.VertexPosProps.Y: pos_y,
            },
            type=nk.VertexType.CUSTOM,
        )
        nodes.append(node)

    # Añadir nodos primarios
    for i, p in iter_prim:
        pos_x = prim_x_pos if axis == ROWS_IDX else NODES_GAP * (i + 1)
        pos_y = NODES_GAP * (i + 1) if axis == ROWS_IDX else prim_y_pos
        node = Vertex(
            id=p,
            data={
                nk.VertexDataProps.LBL: p,
                nk.VertexDataProps.COLOR: n_colors[ROWS_IDX],
                nk.VertexDataProps.VALUE: 0,
            },
            position={
                nk.VertexPosProps.X: pos_x,
                nk.VertexPosProps.Y: pos_y,
            },
            type=nk.VertexType.CUSTOM,
        )
        nodes.append(node)

    return nodes

    # n_colors = get_rnd_colors(BASE_2, spectrum.FormatProp.HEX)

    # INT_TEN = INT_ONE * 10
    # NODES_GAP: int = INT_TEN

    # prim_x_pos = INT_TEN
    # prim_y_pos = NODES_GAP
    # dual_x_pos = INT_TEN
    # dual_y_pos = INT_TEN
    # prim_iter = enumerate(prim, start=NODES_GAP)
    # dual_iter = enumerate(dual, start=INT_TEN)
    # if axis == ROWS_IDX:
    #     prim_x_pos = NODES_GAP
    #     prim_y_pos = INT_TEN
    #     dual_x_pos = INT_TEN
    #     dual_y_pos = INT_TEN
    #     prim_iter = enumerate(prim)
    #     dual_iter = enumerate(dual)

    # nodes = []

    # # Dual nodes (left or bottom)
    # for dei, effect in dual_iter:
    #     for dej, d in enumerate(effect):
    #         node = Vertex(
    #             id=f'{len(nodes)}',
    #             data={
    #                 nk.VertexDataProps.LBL: d,
    #                 nk.VertexDataProps.COLOR: n_colors[COLS_IDX],
    #                 nk.VertexDataProps.VALUE: 0,
    #             },
    #             position={
    #                 nk.VertexPosProps.X: dual_x_pos if axis == ROWS_IDX else dei,
    #                 nk.VertexPosProps.Y: dei if axis == ROWS_IDX else dual_y_pos,
    #             },
    #             type=nk.VertexType.CUSTOM,
    #         )
    #         nodes.append(node)

    # # Primal nodes (right or top)
    # for pci, cause in prim_iter:
    #     for pcj, p in enumerate(cause):
    #         node = Vertex(
    #             id=f'{len(nodes)}',
    #             data={
    #                 nk.VertexDataProps.LBL: p,
    #                 nk.VertexDataProps.COLOR: n_colors[ROWS_IDX],
    #                 nk.VertexDataProps.VALUE: 0,
    #             },
    #             position={
    #                 nk.VertexPosProps.X: prim_x_pos if axis == ROWS_IDX else pci,
    #                 nk.VertexPosProps.Y: pci if axis == ROWS_IDX else prim_y_pos,
    #             },
    #             type=nk.VertexType.CUSTOM,
    #         )
    #         nodes.append(node)

    # return nodes
    """ """
    # def reconstruct_nodes(
    #     prim: list[list[str], list[str]], dual: list[list[str], list[str]], axis: int = ROWS_IDX
    # ) -> list[Vertex]:
    #     n_colors = get_rnd_colors(BASE_2, spectrum.FormatProp.HEX)

    #     # Si el eje es de las filas, el primal estará más a la derecha e iterará sobre el vertical, si el eje es por columnas el primal estará más arriba e iterará sobre el horizontal
    #     NODES_GAP: int = FLOAT_ONE * 10
    #     prim_x_pos: float = NODES_GAP if axis == ROWS_IDX else FLOAT_ONE
    #     prim_y_pos: float = FLOAT_ONE if axis == ROWS_IDX else NODES_GAP

    #     dual_x_pos: float = FLOAT_ONE
    #     dual_y_pos: float = FLOAT_ONE

    #     iter_prim = iterable
    #     iter_dual = iterable

    #     # ! Tal vez el valor es la TPM del elemento en ON [#13] ! #
    #     nodes = [
    #         [
    #             Vertex(
    #                 id=d,
    #                 data={
    #                     nk.VertexDataProps.LBL: d,
    #                     nk.VertexDataProps.COLOR: n_colors[COLS_IDX],
    #                     nk.VertexDataProps.VALUE: 0,
    #                 },
    #                 position={
    #                     nk.VertexPosProps.X: dual_x_pos,
    #                     nk.VertexPosProps.Y: dual_y_pos,
    #                 },
    #                 type=nk.VertexType.CUSTOM,
    #             )
    #             for d in dual[EFFECT]
    #         ],
    #         [
    #             {
    #                 nk.VertexDataProps.LBL: d,
    #                 nk.VertexDataProps.COLOR: n_colors[COLS_IDX],
    #                 nk.VertexDataProps.VALUE: 0,
    #             }
    #             for d in dual[CAUSES]
    #         ],
    #         [
    #             {
    #                 nk.VertexDataProps.LBL: p,
    #                 nk.VertexDataProps.COLOR: n_colors[ROWS_IDX],
    #                 nk.VertexDataProps.VALUE: 0,
    #             }
    #             for p in prim[EFFECT]
    #         ],
    #         [
    #             {
    #                 nk.VertexDataProps.LBL: p,
    #                 nk.VertexDataProps.COLOR: n_colors[ROWS_IDX],
    #                 nk.VertexDataProps.VALUE: 0,
    #             }
    #             for p in prim[CAUSES]
    #         ],
    #     ]
    #     # Flatten the list
    #     nodes = [node for sublist in nodes for node in sublist]

    # vertices = []
    # for de, dc in zip(*dual):
    #     ic(de, dc)
    # for pe, pc in zip(*prim):
    #     ic(pe, pc)

    # nodes.append(Vertex(id=effect, data={nk.VertexDataProps.LBL: effect}))
    # nodes.append(Vertex(id=cause, data={nk.VertexDataProps.LBL: cause}))
    # return nodes


def reconstruct_edges(mip: tuple[tuple[str]]) -> list[Arc]:
    edges = []
    for effect, cause in mip:
        edges.append(Arc(id=f'{cause}-{effect}', source=cause, target=effect))
    return edges
