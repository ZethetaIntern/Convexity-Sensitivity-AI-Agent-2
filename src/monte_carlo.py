import numpy as np
import pandas as pd


def simulate_portfolio_returns(
    mean_return,
    volatility,
    num_simulations=10000,
    time_horizon=252
):
    """
    Generate Monte Carlo simulated portfolio returns.
    """

    simulated_returns = np.random.normal(
        loc=mean_return / time_horizon,
        scale=volatility / np.sqrt(time_horizon),
        size=(time_horizon, num_simulations)
    )

    portfolio_paths = np.cumprod(
        1 + simulated_returns,
        axis=0
    )

    return portfolio_paths


def calculate_var(
    portfolio_values,
    confidence_level=0.95
):
    """
    Calculate Value at Risk (VaR).
    """

    final_values = portfolio_values[-1]
    percentile = (1 - confidence_level) * 100

    var = np.percentile(
        final_values,
        percentile
    )

    return var


def calculate_expected_shortfall(
    portfolio_values,
    confidence_level=0.95
):
    """
    Calculate Expected Shortfall (CVaR).
    """

    final_values = portfolio_values[-1]

    var_threshold = np.percentile(
        final_values,
        (1 - confidence_level) * 100
    )

    expected_shortfall = final_values[
        final_values <= var_threshold
    ].mean()

    return expected_shortfall


def simulation_summary(
    portfolio_values,
    confidence_level=0.95
):
    """
    Generate simulation summary metrics.
    """

    final_values = portfolio_values[-1]

    summary = {
        "Mean Final Value": np.mean(final_values),
        "Median Final Value": np.median(final_values),
        "Minimum Value": np.min(final_values),
        "Maximum Value": np.max(final_values),
        "VaR": calculate_var(
            portfolio_values,
            confidence_level
        ),
        "Expected Shortfall": calculate_expected_shortfall(
            portfolio_values,
            confidence_level
        )
    }

    return pd.DataFrame(
        summary.items(),
        columns=["Metric", "Value"]
    )