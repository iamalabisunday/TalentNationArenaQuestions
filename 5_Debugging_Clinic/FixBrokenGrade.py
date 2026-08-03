# Implement grade_label(score). Return A for scores from 90 to 100, B for scores from 80 to 89, C for scores from 70 to 79, and F for scores below 70. If the score is less than 0 or greater than 100, return Invalid score. This fixes common comparison and branch-order bugs.
def grade_label(score):
    # Bug to fix: branch order and boundary checks must be correct.
    if score < 0 or score > 100:
        return "Invalid score"
    if score >= 90:
        result = "A"
    elif score >= 80:
        result = "B"
    elif score >= 70:
        result = "C"
    elif score < 70:
        result = "F"
    return result