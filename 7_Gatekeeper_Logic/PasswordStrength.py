# Implement password_strength(password). Return Weak if the password has fewer than 8 characters. Return Medium if it has at least 8 characters but does not contain both letters and digits. Return Strong if it has at least 8 characters and contains at least one letter and at least one digit. Students may need to research isalpha and isdigit.

def password_strength(password):
    pass_num = len(password)

    if pass_num < 8:
        return "Weak"

    has_letters = False
    has_digits = False

    if pass_num >= 8:
        for char in password.lower():
            if ("a" <= char <= "z"):
                has_letters = True
            elif ("0" <= char <= "9"): 
                has_digits = True

    if has_letters and has_digits:
        return "Strong"
    else:
        return "Medium"