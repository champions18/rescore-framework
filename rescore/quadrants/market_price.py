import numpy as np
from ..risk_base import BaseRiskModule

class MarketPriceRiskModule(BaseRiskModule):
    def simulate_losses(self, n_sims=10000):
        mean = self.config.get("mean_loss", 40000)
        sigma = self.config.get("sigma", 0.8)
        mu = np.log(mean) - 0.5 * sigma**2
        return np.random.lognormal(mean=mu, sigma=sigma, size=n_sims)
