import pandas as pd


def portfolio_summary(df):

    total_market_value = df["MarketValue_INR"].sum()

    weighted_duration = (
        (df["ModifiedDuration"] * df["PortfolioWeight"]).sum()
    )

    weighted_convexity = (
        (df["Convexity"] * df["PortfolioWeight"]).sum()
    )

    weighted_yield = (
        (df["YieldToMaturity"] * df["PortfolioWeight"]).sum()
    )

    return {
        "Total Market Value": total_market_value,
        "Portfolio Duration": weighted_duration,
        "Portfolio Convexity": weighted_convexity,
        "Portfolio Yield": weighted_yield
    }