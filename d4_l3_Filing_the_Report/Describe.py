"""
An f-string can hold any expression inside its braces, not just a plain variable. Implement describe(name) and return the line name has length N, where N is the number of characters in name, worked out inside the f-string with len(). For Ada the line is Ada has length 3. An empty name has length 0.
"""
def describe(name):
    num = len(name)
    return f"{name} has length {num}"