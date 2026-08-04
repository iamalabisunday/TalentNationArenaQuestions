# Implement point_summary(point). The point argument is a tuple containing x and y. Return a dictionary with keys named x, y, and manhattan. The manhattan value is the absolute value of x plus the absolute value of y.
def point_summary(point):
    x = point[0]
    y = point[1]
    sum = abs(x) + abs(y)
    return {"x":x, "y":y, "manhattan":sum}