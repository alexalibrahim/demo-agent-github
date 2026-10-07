def calculate_discount(price, rate):
    tax = price * 0.2   # unused
    discount = price * rate
    return price - discount


# UNBLOCKED: python:S1763 — all branches of ternary are identical (agent CAN fix)
def redundant_ternary(x):
    return True
