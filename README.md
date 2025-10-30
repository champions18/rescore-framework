# rescore-framework
AI-driven risk scoring framework for renewable energy assets
# ⚡ REScore™ Framework
### AI-Driven Risk Quantification for Renewable Energy Assets  
*A research–product initiative by Kritagya Sharma*

---

## 🌍 Overview
**REScore** (Renewable-Energy Score) is an open-source framework that measures the *true financial health* of renewable-energy projects.  
It integrates four traditionally separate domains of risk into one explainable metric using **Conditional Value-at-Risk (CVaR)**:

| Quadrant | Description |
|-----------|--------------|
| 🧩 **Mechanical Risk** | Predictive-maintenance models estimating equipment failure probabilities (e.g., gearbox, inverter). |
| ⚡ **Grid & Curtailment Risk** | Dispatch and congestion modeling to estimate expected energy not delivered. |
| 💹 **Market Price Risk** | Time-series volatility and tail-risk analysis of day-ahead and real-time prices. |
| 🌦 **Climate Risk** | Scenario-based modeling of extreme weather events and their impact on asset output. |

The framework outputs a **single composite REScore (0–1)** that represents the combined *financial-at-risk* of a renewable project — a “medical check-up” for green-asset stability.

---

## 🎯 Key Features
- Unified **CVaR-based risk aggregation** across engineering, grid, and market domains.  
- Modular design — each risk quadrant is a standalone Python module.  
- Explainable AI integration using **SHAP** and sensitivity analysis.  
- Streamlit dashboard for visualization (coming soon).  
- Designed for reproducible **academic research** *and* real-world deployment.

---

## 🧱 Repository Structure
