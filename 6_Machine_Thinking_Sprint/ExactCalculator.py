# Implement exact_calculator(left, operator, right). Convert left and right to numbers. Support addition, subtraction, multiplication, division, remainder, and exponent. If either number cannot be converted, return Invalid number. If the operator is not supported, return Invalid operator. If division or remainder uses zero on the right side, return Cannot divide by zero. Round numeric results to 2 decimal places.

def exact_calculator(left, operator, right):
    try: 
        num_left = float(left)
        num_right = float(right)

    except (ValueError, TypeError):
        return "Invalid number"

    if (operator == "/" or operator == "%") and num_right == 0:
        return "Cannot divide by zero"

    if operator == "+":
        result = num_left + num_right
    elif operator == "-":
        result = num_left - num_right
    elif operator == "*":
        result = num_left * num_right
    elif operator == "/":
        result = num_left / num_right
    elif operator == "%":
        result = num_left % num_right
    elif operator == "**":
        result = num_left ** num_right
    else:
        return "Invalid operator"

    return round(result, 2)