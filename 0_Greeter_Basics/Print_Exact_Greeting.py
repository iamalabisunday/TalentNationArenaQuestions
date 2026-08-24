# Write a function called `solution` that receives a student's name and returns an exact greeting.

# The greeting must follow this exact format:

# Hello, <name>. Welcome to Talent Nation.

# Rules:
# - Use the name passed into the function.
# - Return the final string.
# - Do not print.
# - Do not hardcode only the sample names.


# def solution(name):
#     return f"Hello, {name}. Welcome to Talent Nation."

# Standard Method
class Solution:
    def __init__(self, name: str):
        self.name = name
    def __str__(self):
        return f"Hello, {self.name}. Welcome to Talent Nation"
    def __repr__(self):
        return f"Solution {self.name}"

def main():
    name = input("Enter a name: ")
    result = Solution(name)
    print("-------------------")
    print(result)
    print("-------------------")

def ask_again():
    while True:
        again = input("Do you want to try again: ").lower().strip()
        if again in ("y", "yes"):
            return True
        elif again in ("n", "now"):
            return False
        print("Invalid: Kindly enter yes or no")

if __name__ == "__main__":
    while True:
        main()
        if not ask_again():
            print("Goodbye!")
            break