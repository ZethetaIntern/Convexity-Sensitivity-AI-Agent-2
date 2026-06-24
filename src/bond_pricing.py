# bond_pricing.py

def bond_price(face_value, coupon_rate, yield_rate, maturity):

    coupon = face_value * coupon_rate

    price = 0

    # Discount coupon payments
    for t in range(1, maturity + 1):

        price += coupon / ((1 + yield_rate) ** t)

    # Discount face value
    price += face_value / ((1 + yield_rate) ** maturity)

    return round(price, 2)