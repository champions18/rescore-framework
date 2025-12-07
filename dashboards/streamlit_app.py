import os
import sys

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)
    

import streamlit as st
import numpy as np
import pandas as pd

from rescore.quadrants.mechanical import MechanicalRiskModule
from rescore.quadrants.grid_curtailment import GridCurtailmentRiskModule
from rescore.quadrants.market_price import MarketPriceRiskModule
from rescore.quadrants.climate import ClimateRiskModule

from rescore.aggregation.cvar import compute_rescore, cvar


# ----------------------------------------
# PAGE SETUP
# ----------------------------------------
st.set_page_config(page_title="REScore Dashboard", layout="wide")

st.title("🔋 REScore – Renewable Energy Risk Dashboard")
st.markdown("""
This dashboard computes a **unified REScore (0–1)** based on four risk quadrants:

- **Mechanical Risk**
- **Grid Curtailment Risk**
- **Market Price Risk**
- **Climate Risk**

All risk distributions are generated through synthetic simulations for demonstration.
""")


# ----------------------------------------
# SIDEBAR CONTROLS
# ----------------------------------------
st.sidebar.header("Simulation Settings")

n_sims = st.sidebar.slider("Number of Monte Carlo Simulations", 1000, 50000, 10000, 1000)
alpha = st.sidebar.slider("CVaR Confidence Level (α)", 0.80, 0.99, 0.95, 0.01)

st.sidebar.markdown("---")
st.sidebar.markdown("### Quadrant Weights")

weights = {
    "mechanical": st.sidebar.number_input("Mechanical Weight", 0.0, 1.0, 0.25, 0.05),
    "grid": st.sidebar.number_input("Grid Curtailment Weight", 0.0, 1.0, 0.25, 0.05),
    "market": st.sidebar.number_input("Market Price Weight", 0.0, 1.0, 0.25, 0.05),
    "climate": st.sidebar.number_input("Climate Risk Weight", 0.0, 1.0, 0.25, 0.05),
}

total_weight = sum(weights.values())
if total_weight != 1.0:
    st.sidebar.error("❌ Total weights must sum to 1.0")
else:
    st.sidebar.success("✔️ Weights valid")


# ----------------------------------------
# RUN SIMULATION
# ----------------------------------------
if st.button("Run REScore Simulation"):
    with st.spinner("Running simulations..."):

        mech_losses = MechanicalRiskModule().simulate_losses(n_sims)
        grid_losses = GridCurtailmentRiskModule().simulate_losses(n_sims)
        mkt_losses = MarketPriceRiskModule().simulate_losses(n_sims)
        clim_losses = ClimateRiskModule().simulate_losses(n_sims)

        # CVaR values per quadrant
        mech_cvar = cvar(mech_losses, alpha)
        grid_cvar = cvar(grid_losses, alpha)
        mkt_cvar = cvar(mkt_losses, alpha)
        clim_cvar = cvar(clim_losses, alpha)

        # Final REScore
        rescore = compute_rescore(
            mech_losses, grid_losses, mkt_losses, clim_losses,
            alpha=alpha, weights=weights, scale=1e6
        )

    st.success("Simulation Complete!")

    # ----------------------------------------
    # RESULTS – SCORE
    # ----------------------------------------
    st.subheader("📊 Final REScore")
    st.metric("REScore (0–1 scale)", f"{rescore:.4f}")

    # ----------------------------------------
    # RESULTS – CVaR TABLE
    # ----------------------------------------
    st.subheader("Risk Quadrant CVaR Values (monetary units)")

    df_cvar = pd.DataFrame({
        "Quadrant": ["Mechanical", "Grid Curtailment", "Market Price", "Climate"],
        "CVaR": [mech_cvar, grid_cvar, mkt_cvar, clim_cvar]
    })

    st.dataframe(df_cvar, use_container_width=True)

    # ----------------------------------------
    # LOSS DISTRIBUTION VISUALIZATION
    # ----------------------------------------
    st.subheader("Loss Distribution Comparison")

    df_losses = pd.DataFrame({
        "Mechanical": mech_losses,
        "Grid": grid_losses,
        "Market": mkt_losses,
        "Climate": clim_losses,
    })

    st.line_chart(df_losses)


# ----------------------------------------
# FOOTER
# ----------------------------------------
st.markdown("---")
st.markdown("Built with ❤️ for renewable energy risk research.")
