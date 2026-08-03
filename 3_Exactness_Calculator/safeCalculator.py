# Implement safe_calculator(a, operator, b). Return the result of applying the operator to the two numbers. Supported operators are "+", "-", "*", "/", "%", and "**". If the operator is unknown, return "Invalid operator". If the operator is "/" or "%" and b is 0, return "Cannot divide by zero". Round division results to 2 decimal places.

def safe_calculator(a, operator, b):
    if (operator == "/" or operator == "%") and b == 0:
        return "Cannot divide by zero"
    if operator == "+":
        result = a + b
    elif operator == "-":
        result = a - b
    elif operator == "*":
        result = a * b
    elif operator == "/":
        div = a / b
        result = round(div, 2)
    elif operator == "%":
        result = a % b
    elif operator == "**":
        result = a ** b
    else:
        result = "Invalid operator"
    return result