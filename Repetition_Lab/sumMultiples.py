# Implement sum_multiples(limit, divisor). Return the sum of all positive numbers from 1 to limit inclusive that are divisible by divisor. If divisor is zero, return Invalid divisor. Do not use the built-in sum function.

def sum_multiples(limit, divisor):
    if divisor == 0:
        return "Invalid divisor"
    
    result = []
    total = 0
    for n in range (1, limit + 1):
        if n % divisor == 0:
            result.append(n)

    for char in result:
        total += int(char)
    
    return total
