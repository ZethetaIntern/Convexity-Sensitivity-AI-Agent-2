import pandas as pd

bond_df = pd.read_csv("data/raw/Bond_portfolio_data.csv")

print("\nTotal Columns:", len(bond_df.columns))
print("\nColumn Names:\n")

for col in bond_df.columns:
    print(col)