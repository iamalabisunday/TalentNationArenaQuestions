"""
Two different ways of turning a decimal into a whole number give two different answers, and you must show both. Implement truncate_vs_round(value), where value is a decimal number. Return one line: the result of int() (which drops the fractional part toward zero), the word or with a space on each side, then the result of round() (which rounds to the nearest whole, and to the nearest even number when the value is exactly halfway). For 3.7 the line is 3 or 4.
"""
def truncate_vs_round(value):
    result_int = int(value)
    result_round = round(value)
    return f"{result_int} or {result_round}"