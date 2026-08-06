"""
Now act on the check. Implement safe_quantity(raw), where raw is a string from a form. If the trimmed text is made up only of digits, return it converted to a whole number. Otherwise return the string invalid. A program that crashes on the first bad character is broken, so reject bad input rather than letting it fail. For the form 42 return the number 42; for the form abc return the string invalid.
"""
def safe_quantity(raw):
    num = raw.strip()
    if not num:
        return "invalid"
    for n in num:
        if not ("0" <= n <= "9"):
            return "invalid"
    result = int(num)
    return result