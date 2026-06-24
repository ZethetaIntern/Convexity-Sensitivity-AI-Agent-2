# yield_curve.py

import pandas as pd
import matplotlib.pyplot as plt

def load_yield_curve(file_path):
    """
    Load yield curve data from CSV.
    """
    df = pd.read_csv(file_path)
    return df

def plot_yield_curve(df):
    """
    Plot yield curve from maturity and yield columns.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(df['Maturity'], df['Yield'], marker='o')
    plt.title('Yield Curve')
    plt.xlabel('Maturity')
    plt.ylabel('Yield (%)')
    plt.grid(True)
    plt.show()

def get_yield_spread(df):
    """
    Calculate spread between longest and shortest maturity yields.
    """
    return df['Yield'].iloc[-1] - df['Yield'].iloc[0]

def classify_curve(df):
    """
    Classify yield curve shape.
    """
    spread = get_yield_spread(df)

    if spread > 0.5:
        return "Normal"
    elif spread < -0.5:
        return "Inverted"
    else:
        return "Flat"