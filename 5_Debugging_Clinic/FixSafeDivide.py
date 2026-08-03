# Implement safe_divide(a, b). Return a divided by b rounded to 2 decimal places. If b is zero, return Cannot divide by zero. This fixes the common ZeroDivisionError bug.
def safe_divide(a, b):
    # Bug to fix: dividing by zero crashes the program.
    a = int(a)
    b = int(b)
    if b == 0:
        return "Cannot divide by zero"
    div = a / b
    result = round(div, 2)
    return result