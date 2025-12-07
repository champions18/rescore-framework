REScore Framework

A unified, CVaR-driven risk engine for renewable energy portfolios with an interactive Streamlit dashboard.

⭐ Key Highlights

✔ Modular risk quadrants (Mechanical, Grid, Market, Climate)
✔ CVaR-based aggregation engine
✔ Monte Carlo simulation backend
✔ Ready-to-extend plugin architecture
✔ Streamlit dashboard for real-time exploration
✔ Fully open-source & MIT Licensed

📐 Architecture Overview

flowchart TD

subgraph RESCORE["REScore Framework"]
    direction TB

    subgraph Quadrants["Risk Quadrants"]
        direction LR
        M["Mechanical Risk<br/>(Lognormal / PHM-ready)"]
        G["Grid Curtailment Risk<br/>(Dispatch / Congestion)"]
        P["Market Price Risk<br/>(Monte Carlo / GARCH-ready)"]
        C["Climate Risk<br/>(Exponential / Extremes)"]
    end

    M --> L1["Loss Samples"]
    G --> L2["Loss Samples"]
    P --> L3["Loss Samples"]
    C --> L4["Loss Samples"]

    subgraph Aggregation["CVaR Aggregation Engine"]
        direction TB
        VaR["VaR Computation"]
        CVaR["CVaR Tail Expectation"]
        Weight["Weighted Loss Integration"]
    end

    L1 --> VaR
    L2 --> VaR
    L3 --> VaR
    L4 --> VaR

    VaR --> CVaR --> Weight
    Weight --> Score["Final REScore (0–1)"]
end

Score --> UI["Streamlit Dashboard<br/>(Visualizations & Controls)"]

✨ Features
🔹 Risk Quadrants

Each quadrant exposes a .simulate() method to produce loss distributions.

Mechanical Risk – reliability failures modeled with lognormal distributions

Grid Curtailment Risk – energy lost due to grid constraints

Market Price Risk – volatility of power prices

Climate Risk – extreme weather-driven losses

🔹 CVaR Aggregation Engine

Computes VaR, CVaR, and tail-weighted loss

Produces final 0–1 normalized REScore

🔹 Streamlit Dashboard

Interactive sliders for risk weights

Adjustable Monte Carlo sample size

Distribution plots + CVaR tail shading

Real-time computed REScore

📦 Installation
git clone https://github.com/champions18/rescore-framework.git
cd rescore-framework
pip install -r requirements.txt

📂 Directory Structure
rescore-framework/
│
├── rescore/
│   ├── quadrants/
│   │   ├── mechanical.py
│   │   ├── grid.py
│   │   ├── market.py
│   │   ├── climate.py
│   │   └── __init__.py
│   │
│   ├── aggregation/
│   │   ├── cvar_engine.py
│   │   └── __init__.py
│   │
│   ├── utils/
│   │   ├── distributions.py
│   │   └── __init__.py
│   │
│   └── __init__.py
│
├── dashboards/
│   └── streamlit_app.py
│
├── examples/
│   └── demo_rescore.py
│
├── LICENSE
└── README.md

🚀 Quick Start
▶️ Run the Demo
python -m examples.demo_rescore


Expected Output (example):

Mechanical Loss Mean:      49,654.31
Grid Curtailment Loss:     30,111.69
Market Price Loss:         40,209.49
Climate Loss:              24,958.81

Final REScore (0–1 scale): 0.9219

🖥 Run the Streamlit Dashboard
streamlit run dashboards/streamlit_app.py


This opens an interactive UI with:

Loss distribution plots

CVaR tail region visualization

Risk weight sliders

Final REScore indicator

📊 Example Visual Outputs (Add Screenshots Later)

You can add images like this once screenshots are ready:

![Dashboard Screenshot](images/dashboard.png)

🛣 Roadmap

 Integrate GARCH for price volatility

 Add SCADA-driven mechanical reliability forecasting

 Add Extreme Value Theory (GEV/POT) for climate tails

 Export PDF risk reports

 Add SHAP-based explainability for REScore

🤝 Contributing

Pull requests are welcome!
For major changes, please open an issue first to discuss what you’d like to modify.
