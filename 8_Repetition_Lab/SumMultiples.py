# Implement sum_multiples(limit, divisor). Return the sum of all positive numbers from 1 to limit inclusive that are divisible by divisor. If divisor is zero, return Invalid divisor. Do not use the built-in sum function.
def sum_multiples(limit, divisor):
    if divisor == 0:
        return "Invalid divisor"
    result = 0
    for char in range(1, limit + 1):
        if char > 0 and char % divisor == 0:
            result += char
    return result