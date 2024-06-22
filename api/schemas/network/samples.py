DEFFAULT_NETWORK_EXAMPLE = {
    'example': {
        # 'id': '5f3d3c0e0b3e3d3e3d3c0e0b',
        'vertices': [
            {
                'id': '1',
                'data': {
                    'label': 'node 0',
                    'color': '#a3f3ce',
                    'value': 1.0
                },
                'position': {
                    'x': 0.0,
                    'y': 0.0
                },
                'type': 'custom'
            },
            {
                'id': '2',
                'data': {
                    'label': 'node 1',
                    'color': '#423fce',
                    'value': 0.2
                },
                'position': {
                    'x': 0.0,
                    'y': 0.0
                },
                'type': 'custom'
            }
        ],
        'arcs': [
            {
                'id': '1-2',
                'source': '1',
                'target': '2',
                'data': {
                    'color': '#999fff',
                    'weight': 12,
                },
                'animated': False,
                'type': 'custom'
            }
        ],
        'info': {
            'label': 'Net ¿?',
            'is_complete': False,
            'is_connected': False,
            'is_weighted': False,
            'is_directed': False,
            'is_k_bipartite': False,
            'k_degree': -1
        }
    }
}
