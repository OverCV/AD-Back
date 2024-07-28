import pyphi

"""The network shown in Figure 4 of the 2014 IIT 3.0 paper.

    Diagram::

                +~~~~~~~+
          +~~~~>|   A   |<~~~~+
          | +~~~+ (OR)  +~~~+ |
          | |   +~~~~~~~+   | |
          | |               | |
          | v               v |
        +~+~~~~~+       +~~~~~+~+
        |   B   |<~~~~~~+   C   |
        | (AND) +~~~~~~>| (XOR) |
        +~~~~~~~+       +~~~~~~~+

    tpm = np.array([
        [0, 0, 0], # 0
        [0, 0, 1], # 1
        [1, 0, 1], # 3
        [1, 0, 0], # 4
        [1, 0, 0], # 4
        [1, 1, 1], # 7
        [1, 0, 1], # 5
        [1, 1, 0], # 6
    ])
"""

net = pyphi.examples.fig4()
num_nodes = net.cm.shape[1]

# Obtener los istates:

bg_nodes = (0, 1, 2)
istate = (0, 1, 0)

subsys = pyphi.Subsystem(
    network=net,
    state=istate,
    nodes=bg_nodes,
)
