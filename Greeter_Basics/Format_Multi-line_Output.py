# Write a function called `solution` that receives a student's name and cohort, then returns a three-line badge.

# The badge must follow this exact format:

# Name: <name>
# Cohort: <cohort>
# Status: Ready

# Rules:
# - Use newline characters between the lines.
# - Do not add extra spaces.
# - Do not add an extra blank line at the end.
# - Return the final string.

def solution(name, cohort):
    return (
        f"Name: {name}\n"
        f"Cohort: {cohort}\n"
        f"Status: Ready"
    )