# Implement arithmetic_engine(a, b). Return a dictionary with three keys: "sum", "product", and "power". The sum is a + b, the product is a * b, and the power is a ** b.

def arithmetic_engine(a, b):
    a_val = int(a)
    b_val = int(b)
    sum = a_val + b_val
    product = a_val * b_val
    power = a_val ** b_val
    return {"sum":sum, "power": power, "product": product}