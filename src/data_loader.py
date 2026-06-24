 # data_loader.py

import pandas as pd


def load_bond_data(file_path):
    """
    Load bond dataset from CSV file.
    """
    try:
        df = pd.read_csv(file_path)
        print(f"Bond data loaded successfully: {df.shape}")
        return df
    except Exception as e:
        print(f"Error loading bond data: {e}")
        return None


def load_portfolio_data(file_path):
    """
    Load portfolio dataset from CSV file.
    """
    try:
        df = pd.read_csv(file_path)
        print(f"Portfolio data loaded successfully: {df.shape}")
        return df
    except Exception as e:
        print(f"Error loading portfolio data: {e}")
        return None


def load_yield_curve_data(file_path):
    """
    Load yield curve dataset from CSV file.
    """
    try:
        df = pd.read_csv(file_path)
        print(f"Yield curve data loaded successfully: {df.shape}")
        return df
    except Exception as e:
        print(f"Error loading yield curve data: {e}")
        return None


def get_dataset_summary(df):
    """
    Return dataset summary statistics.
    """
    return {
        "Rows": df.shape[0],
        "Columns": df.shape[1],
        "Column Names": list(df.columns),
        "Missing Values": df.isnull().sum().to_dict()
    }