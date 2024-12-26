# Árbol de directorios
Árbol de directorios:

```ps
project_root/
│
├── .venv/
│   └── .dev.env
│
├── api/
│   ├── middlewares/
│   │   ├── exception.py
│   │   └── profiling.py
│   │
│   ├── models/
│   │   ├── bnb/
│   │   │   └── nodum.py
│   │   │
│   │   ├── enums/
│   │   │   ├── database.py
│   │   │   ├── backend.py
│   │   │   ├── extensions.py       ! File extensions to use.
│   │   │   └── frontend.py
│   │   │
│   │   ├── genetic/
│   │   │   ├── individual.py
│   │   │   ├── population.py
│   │   │   ├── environ.py
│   │   │   └── recorder.py
│   │   │
│   │   ├── network/
│   │   │   ├── edge.py
│   │   │   ├── info.py
│   │   │   ├── network.py
│   │   │   └── node.py
│   │   │
│   │   ├── props/                  !! Revisar clase pues hay puntos relevantes con lógica difusa
│   │   │   ├── analisis.py         ! (unused) Intento de objetizar el retorno con TypedDict
│   │   │   ├── network.py          ! Para frontend
│   │   │   ├── sia.py              ! Intento de objetizar net
│   │   │   ├── spectrum.py
│   │   │   └── structure.py
│   │   │
│   │   ├── queyranne/
│   │   │   └── deletion.py
│   │   │
│   │   ├── matrix.py
│   │   ├── nodum.py
│   │   ├── structure.py
│   │   └── system.py
│   │
│   ├── routes/
│   │   ├── analyze.py
│   │   ├── metrics.py
│   │   ├── network.py
│   │   ├── server.py
│   │   └── structure.py
│   │
│   ├── schemas/
│   │   ├── genetic/
│   │   │   └── control.py
│   │   │
│   │   ├── network/
│   │   │   ├── arc.py
│   │   │   ├── info.py
│   │   │   ├── samples.py
│   │   │   ├── schema.py
│   │   │   └── vertex.py
│   │   │
│   │   ├── networks.py
│   │   ├── sample.py
│   │   └── structure.py
│   │
│   ├── services/                   ! RELEVANT
│   │   ├── analyze/
│   │   │   ├── strats/
│   │   │   │   ├── branch.py
│   │   │   │   ├── force.py
│   │   │   │   ├── frank_mech.py
│   │   │   │   ├── genetic.py
│   │   │   │   ├── metrics.py
│   │   │   │   ├── qredges.py
│   │   │   │   └── qrnodes.py
│   │   │   ├── compute.py
│   │   │   └── sia.py
│   │   │   
│   │   ├── structure/
│   │   │   └── base.py
│   │   │   
│   │   └── network.py
│   │
│   └── shared/
│       ├── network/
│       │   └── algo.py
│       │
│       ├── validators/
│       │   ├── analyze.py
│       │   └── structure.py
│       │
│       └── formatter.py
│
├── assets/
│   ├── tpm_n2s/
│   │   ├── F3.xlsx
│   │   ├── F4.xlsx
│   │   ├── ...
│   │   ├── F15.xlsx
│   │   └── QRNodes.xlsx
│   │
│   └── tpm_n2s/
│       └── S4S.xlsx
│
├── data/
│   ├── base/
│   │   └── .sqlite
│   │
│   ├── profiles/
│   │   ├── analyze_sia-pyphi.html      ! Should assign net&subsystem on name
│   │   ├── analyze_sia-qredges.html
│   │   ├── ...
│   │   └── analyze_sia-qrnodes.html
│   │
│   ├── reports/
│   │   ├── reporte_metricas.xlsx
│   │   └── QRNodes.html                ! Repeated in assets?
│   │
│   ├── motors.py
│   └── tables.py
│
├── docs/
│   ├── all.plantuml
│   ├── app.md
│   ├── branch-cd.plantuml
│   ├── genetic-sd.plantuml
│   ├── genetics-cd.plantuml
│   ├── Guía_de_instalación.md
│   ├── margin.md
│   └── three.md
│
├── constants/
│   ├── format.py
│   ├── genetic.py
│   └── structure.py
│
├── utils/
│   ├── color.py
│   ├── consts.py
│   ├── funcs.py
│   ├── network.py
│   └── pairs.py
│
├── tests/
│   └── ...
│
├── exec.py
├── main.py
├── server.py
│
├── pyphi_config.py
├── README.md
└── requirements.txt
```