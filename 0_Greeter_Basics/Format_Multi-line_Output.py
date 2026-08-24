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

# def solution(name, cohort):
#     return (
#         f"Name: {name}\n"
#         f"Cohort: {cohort}\n"
#         f"Status: Ready"
#     )

class Solution:
    def __init__(self, name: str, cohort: str):
        self.name = name
        self.cohort = cohort

    def __str__(self):
        return (
            f"Name: {self.name}\n"
            f"Cohort: {self.cohort}\n"
            f"Status: Ready"
        )

    def __repr__(self):
        return f"Solution: '{self.name}', {self.cohort}"

def ask_to_continue():
    while True:
        again = input("Do you want to try again: ").strip().lower()
        if again in ("y", "yes"):
            return True
        elif again in ("n", "now"):
            return False
        print("Invalid choice. Please enter 'y' or 'n'.")

def main():
    print("---------Solution-----------")

    name = input("Enter name: ")
    cohort = input("Enter cohort: ")

    result = Solution(name, cohort)
    print("-------------------")
    print(result)
    print("-------------------")
    
if __name__ == "__main__":
    while True:
        main()
        if not ask_to_continue():
            print("\nGoodBye")
            break