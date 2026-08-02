# Implement top_scorer(scores). The scores argument is a dictionary mapping student names to numeric scores. Return the name of the student with the highest score. If the dictionary is empty, return No scores. If there is a tie, return the name that comes first alphabetically.

def top_scorer(scores):
    # Guard clause for empty dictionary
    if not scores:
        return "No scores"
    
    best_student = None
    highest_score = None
    
    # Manually inspect every student-score pair
    for student, score in scores.items():
        if highest_score is None:
            # First item seen initializes our tracking variables
            best_student = student
            highest_score = score
        elif score > highest_score:
            # Found a strictly higher score
            best_student = student
            highest_score = score
        elif score == highest_score:
            # Tie breaker: keep the name that comes first alphabetically
            if student < best_student:
                best_student = student

    return best_student