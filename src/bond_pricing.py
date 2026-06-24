# bond_pricing.py

import numpy as np


def bond_price(face_value, coupon_rate, yield_rate, years_to_maturity, frequency=2):
    """
    Calculate bond price using discounted cash flows.

    Parameters:
        face_value (float): Face/par value of bond
        coupon_rate (float): Annual coupon rate (e.g. 0.05 for 5%)
        yield_rate (float): Annual yield to maturity (e.g. 0.06 for 6%)
        years_to_maturity (float): Years remaining until maturity
        frequency (int): Coupon payments per year

    Returns:
        float: Bond price
    """

    periods = int(years_to_maturity * frequency)

    coupon_payment = (
        face_value * coupon_rate / frequency
    )

    discount_rate = yield_rate / frequency

    cash_flows = np.full(periods, coupon_payment)
    cash_flows[-1] += face_value

    discount_factors = [
        (1 + discount_rate) ** t
        for t in range(1, periods + 1)
    ]

    price = np.sum(
        cash_flows / np.array(discount_factors)
    )

    return price


def current_yield(face_value, coupon_rate, market_price):
    """
    Calculate current yield.
    """

    annual_coupon = face_value * coupon_rate

    return annual_coupon / market_price


def price_change_percentage(old_price, new_price):
    """
    Calculate percentage price change.
    """

    return ((new_price - old_price) / old_price) * 100