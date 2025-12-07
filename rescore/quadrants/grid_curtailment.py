import numpy as np
from ..risk_base import BaseRiskModule

class GridCurtailmentRiskModule(BaseRiskModule):
    def simulate_losses(self, n_sims=10000):
        mean = self.config.get("mean_loss", 30000)
        std = self.config.get("std_loss", 10000)
        return np.random.normal(loc=mean, scale=std, size=n_sims).clip(min=0)
