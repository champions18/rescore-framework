from abc import ABC, abstractmethod
import numpy as np

class BaseRiskModule(ABC):
    def __init__(self, config=None):
        self.config = config or {}

    @abstractmethod
    def simulate_losses(self, n_sims: int = 10000) -> np.ndarray:
        pass
