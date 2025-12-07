import numpy as np

def cvar(losses: np.ndarray, alpha: float = 0.95) -> float:
    losses = np.asarray(losses)
    var = np.quantile(losses, alpha)
    tail = losses[losses >= var]
    return tail.mean()

def compute_rescore(
    mech_losses,
    grid_losses,
    mkt_losses,
    clim_losses,
    alpha: float = 0.95,
    weights=None,
    scale: float = 1e6
):
    weights = weights or {
        "mechanical": 0.25,
        "grid": 0.25,
        "market": 0.25,
        "climate": 0.25
    }

    total_losses = (
        weights["mechanical"] * mech_losses +
        weights["grid"] * grid_losses +
        weights["market"] * mkt_losses +
        weights["climate"] * clim_losses
    )

    raw = cvar(total_losses, alpha)
    return float(np.exp(-raw / scale))
