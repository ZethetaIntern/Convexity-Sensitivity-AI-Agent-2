def portfolio_duration(df):
    return (
        df["ModifiedDuration"] *
        df["PortfolioWeight"]
    ).sum()

def portfolio_convexity(df):
    return (
        df["Convexity"] *
        df["PortfolioWeight"]
    ).sum()