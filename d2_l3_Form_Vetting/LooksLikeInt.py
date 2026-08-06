"""
Before the stores accept a number, they check that it could be one. Implement looks_like_int(raw), where raw is a string straight off a form. Return True if, after trimming spaces from both ends, the text is made up only of digits, and False otherwise. A minus sign, a decimal point, letters, or an empty form all make it False. Trim the spaces first, then test the digits.
"""
def looks_like_int(raw):
    num = raw.strip()
    if not num:
        return False
    if num == " ":
        return False
    if num == "-":
        return False
    for n in num:
        if not ("0" <= n <= "9"):
            return False
    return True