# Implement top_scorer(scores). The scores argument is a dictionary mapping student names to numeric scores. Return the name of the student with the highest score. If the dictionary is empty, return No scores. If there is a tie, return the name that comes first alphabetically.
def top_scorer(scores):
    if not scores:
        return "No scores"

    top_student = None
    highest_score = None

    for name, score in scores.items():
        if highest_score is None or score > highest_score:
            highest_score = score
            top_student = name

        elif score == highest_score:
            if name < top_student:
                top_student = name

    return top_student

# basic top scorer
# Input: [{"Ada":90,"Tunde":85,"Halima":95}]
# Expected: "Halima"
# single scorer
# Input: [{"Ada":70}]
# Expected: "Ada"ss