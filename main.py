import pandas as pd

from src.risk_metrics import portfolio_summary

bond_df = pd.read_csv(
    "data/raw/Bond_portfolio_data.csv"
)

results = portfolio_summary(bond_df)

for k, v in results.items():
    print(f"{k}: {v}")