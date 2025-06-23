fractal-quantum-gravity/
├── simulations/               # All simulation codes
│   ├── adaptive_rg/          # RG flow simulations
│   │   ├── fractal_rg.py      # Main simulation class
│   │   ├── entropy_constraint.py
│   │   └── run_simulation.py  # Startup script
│   └── cosmology/             # Cosmological simulations
│       ├── inflation.py
│       └── dark_matter.py
├── data/                      # Simulation outputs
│   ├── rg_flow/               # RG flow data
│   │   ├── lambda_flow.csv
│   │   └── dimension_evolution.h5
│   └── desi/                  # DESI test data
│       ├── bao_anomalies.npy
│       └── fractal_dimension_z.csv
├── results/                   # Analysis results
│   ├── figures/               # Automatically generated graphics
│   └── tables/                # Performance metrics
├── docs/                       # Instruction manual
│   └── REPRODUCIBILITY.md      # Reproduction of results
└── requirements.txt            # Required Python libraries
