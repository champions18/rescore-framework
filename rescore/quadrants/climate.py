import numpy as np
from ..risk_base import BaseRiskModule

class ClimateRiskModule(BaseRiskModule):
    def simulate_losses(self, n_sims=10000):
        base = self.config.get("base_loss", 20000)
        tail = self.config.get("tail_scale", 100000)

        # Normal climate variability (small losses)
        base_losses = np.random.exponential(scale=base, size=n_sims)

        # Extreme climate events (rare but huge losses)
        extreme_events = np.random.binomial(
            1, 0.05, size=n_sims
        ) * np.random.exponential(scale=tail, size=n_sims)

        return base_losses + extreme_events
