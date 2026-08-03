# Implement next_age(age_text). The function receives age as text. Convert it to an integer and return the age next year. This fixes the common bug where text is used like a number.
def next_age(age_text):
    # Bug to fix: age_text is text, so convert it before adding.
    age_cov = int(age_text)
    result = age_cov + 1
    return result