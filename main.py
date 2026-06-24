import pandas as pd
from src.risk_metrics import portfolio_summary

bond_df = pd.read_csv("data/raw/Bond_portfolio_data.csv")

bond_df.columns = bond_df.columns.str.strip()

results = portfolio_summary(bond_df)

for metric, value in results.items():
    print(f"{metric}: {value}")