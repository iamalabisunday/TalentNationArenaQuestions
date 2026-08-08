"""
Bearings are always reported to exactly two decimal places. Implement format_bearing(degrees) and return the bearing as a string with two digits after the decimal point, using an f-string format specifier. A bearing of 90 reports as 90.00, and 3.14159 reports as 3.14. The specifier rounds for you.
"""
def format_bearing(degrees):
    return f"{degrees:.2f}"