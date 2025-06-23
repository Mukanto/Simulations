import numpy as np
import h5py
from scipy.integrate import solve_ivp

class FractalRGSimulator:
    """Adaptif RG akışı ile fraktal boyut evrimi"""
    def __init__(self, D0=3.98, lambda_val=0.1, mu_range=(1e-3, 1e19)):
        self.D0 = D0  # IR sınırında başlangıç boyutu
        self.lambda_val = lambda_val  | Renormalizasyon sabiti
        self.mu_min, self.mu_max = mu_range
        
    def beta_D(self, mu, D):
        """Boyut RG akış fonksiyonu"""
        return -0.05 * self.lambda_val**2 * (D - 2)**3 / np.log(mu)
    
    def run_flow(self, steps=1000):
        """RG akışını çöz"""
        mu_points = np.logspace(np.log10(self.mu_min), np.log10(self.mu_max), steps)
        solution = solve_ivp(
            lambda mu, D: self.beta_D(mu, D),
            [self.mu_min, self.mu_max],
            [self.D0],
            t_eval=mu_points
        )
        return solution.t, solution.y[0]

    def save_data(self, filename="data/rg_flow/dimension_evolution.h5"):
        """Çıktıları HDF5 formatında kaydet"""
        mu, D = self.run_flow()
        with h5py.File(filename, 'w') as hf:
            hf.create_dataset('mu', data=mu)
            hf.create_dataset('D', data=D)
