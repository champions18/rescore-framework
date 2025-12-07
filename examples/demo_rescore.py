import numpy as np

from rescore.quadrants.mechanical import MechanicalRiskModule
from rescore.quadrants.grid_curtailment import GridCurtailmentRiskModule
from rescore.quadrants.market_price import MarketPriceRiskModule
from rescore.quadrants.climate import ClimateRiskModule

from rescore.aggregation.cvar import compute_rescore


def main():
    print("\n--- Running REScore Synthetic Demo ---\n")

    n_sims = 10000  # number of Monte Carlo simulations

    # Instantiate each quadrant module
    mech_model = MechanicalRiskModule()
    grid_model = GridCurtailmentRiskModule()
    mkt_model = MarketPriceRiskModule()
    clim_model = ClimateRiskModule()

    # Generate simulated loss distributions
    mech_losses = mech_model.simulate_losses(n_sims)
    grid_losses = grid_model.simulate_losses(n_sims)
    mkt_losses = mkt_model.simulate_losses(n_sims)
    clim_losses = clim_model.simulate_losses(n_sims)

    # Compute final REScore
    score = compute_rescore(
        mech_losses,
        grid_losses,
        mkt_losses,
        clim_losses,
        alpha=0.95
    )

    print(f"Mechanical Loss Mean:       {np.mean(mech_losses):,.2f}")
    print(f"Grid Curtailment Loss Mean: {np.mean(grid_losses):,.2f}")
    print(f"Market Price Loss Mean:     {np.mean(mkt_losses):,.2f}")
    print(f"Climate Loss Mean:          {np.mean(clim_losses):,.2f}")
    print("\n---------------------------------------")
    print(f"Final REScore (0–1 scale):  {score:.4f}")
    print("---------------------------------------\n")


if __name__ == "__main__":
    main()
