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

# def solution(name, a, b, c):
#     sum = a + b + c
#     average = sum / 3
#     average_round = round(average, 2)
#     maximum = max(a,b,c)
#     return (
#     f"Student: {name}\n"
#     f"Sum: {sum}\n"
#     f"Average: {average_round}\n"
#     f"Maximum: {maximum}"
#     )

class SolutionStudent:
    def __init__(self, name: str, a: float, b: float, c: float):
        self.name = name
        self.a = a
        self.b = b
        self.c = c

    def sum(self):
        return self.a + self.b + self.c
    
    def average(self):
        return self.sum() / 3 

    def average_round(self):
        return round(self.average(), 2)

    def maximum(self):
        return max(self.a, self.b, self.c)

    def __str__(self):
        return (
            f"Student: {self.name}\n"
            f"Sum: {self.sum()}\n"
            f"Average: {self.average_round()}\n"
            f"Maximum: {self.maximum()}"
        )

    def __repr__(self):
        return f"SolutionStudent('{self.name}', {self.a}, {self.b}, {self.c})"


# --- Standalone Helper & Script Functions ---

def get_float_input(prompt: str) -> float:
    """Helper function to keep prompting until a valid number is entered."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a numerical score.")


def ask_to_continue() -> bool:
    """Prompts the user to continue and returns True if 'y', False if 'n'."""
    while True:
        choice = input("\nDo you want to add another student? (y/n): ").strip().lower()
        if choice in ("y", "yes"):
            return True
        if choice in ("n", "no"):
            return False
        print("Invalid choice. Please enter 'y' or 'n'.")


def main():
    print("=== Student Grade Calculator ===")
    
    name = input("\nEnter student name: ").strip()
    a = get_float_input("Enter grade 1: ")
    b = get_float_input("Enter grade 2: ")
    c = get_float_input("Enter grade 3: ")

    # Create the object instance
    student = SolutionStudent(name, a, b, c)

    # Print informal string output (__str__)
    print("\n" + "=" * 25)
    print(student)
    print("=" * 25)

    # Inspect the object state (__repr__)
    print(f"\nDeveloper Repr: {repr(student)}")


if __name__ == "__main__":
    while True:
        main()
        if not ask_to_continue():
            print("\nGoodbye!")
            break