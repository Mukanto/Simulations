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

** DATASETS & FORMATS **
# RG Flow Data(lambda_flow.csv):

mu, D, beta_D
1e-3, 3.982, 0.00021
1e-2, 3.978, 0.00054
... 
1e19, 2.001, -0.185

# DESI Anomaly Data(bao_anomalies.npy):

- Size: (1000, 3) (z, δD/D, error)
- Recovery code(python):
data = np.load('data/desi/bao_anomalies.npy')
redshifts = data[:,0]
anomalies = data[:,1]

# Cosmological Constant Evolution(lambda_evolution.h5)[python]:

with h5py.File('data/cosmology/lambda_evolution.h5', 'r') as hf:
    mu = hf['mu'][:]
    Lambda = hf['Lambda'][:]

    
