# Write a function called `solution` that converts kilograms to grams and pounds.

# The function receives one value, `kilograms`, and must return a three-line report in this exact format:

# Kilograms: <kilograms>
# Grams: <grams>
# Pounds: <pounds>

# Rules:
# - Convert the input to a number using `float()`.
# - 1 kilogram = 1000 grams.
# - 1 kilogram = 2.20462 pounds.
# - Round pounds to 2 decimal places.
# - Return the final multi-line string.
# - Do not print.

def solution(kilograms):
    kilograms_float = float(kilograms)
    grams = float(kilograms_float * 1000)
    pounds = float(kilograms_float * 2.20462)
    pounds_dec = round(pounds, 2)
    return (
        f"Kilograms: {kilograms_float}\n"
        f"Grams: {grams}\n"
        f"Pounds: {pounds_dec}"
    )