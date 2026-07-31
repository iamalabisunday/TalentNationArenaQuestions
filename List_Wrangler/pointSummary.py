# Implement point_summary(point). The point argument is a tuple containing x and y. Return a dictionary with keys named x, y, and manhattan. The manhattan value is the absolute value of x plus the absolute value of y.
def point_summary(point):
    x, y = point
    x = int(x)
    y = int(y)
    
    manhattan_val = abs(x) + abs(y)
    
    return {
        "x": x,
        "y": y,
        "manhattan": manhattan_val
    }