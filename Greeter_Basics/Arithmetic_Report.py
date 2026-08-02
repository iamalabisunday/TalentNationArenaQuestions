# Write a function called `solution` that receives a student's name and three numbers.

# Return a four-line report in this exact format:

# Student: <name>
# Sum: <sum>
# Average: <average>
# Maximum: <maximum>

# Rules:
# - Add the three numbers to get the sum.
# - Divide the sum by 3 to get the average.
# - Round the average to 2 decimal places.
# - Find the largest number.
# - Return the final multi-line string.
# - Do not print.

def solution(name, a, b, c):
    sum = a + b + c
    average = sum / 3
    average_round = round(average, 2)
    maximum = max(a,b,c)
    return (
    f"Student: {name}\n"
    f"Sum: {sum}\n"
    f"Average: {average_round}\n"
    f"Maximum: {maximum}"
    )