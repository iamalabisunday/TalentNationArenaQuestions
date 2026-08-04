# Implement triangle_pattern(n). Return a string containing a left-aligned triangle of asterisks with n rows. Row 1 has one asterisk, row 2 has two asterisks, and so on. Lines should be separated by newline characters. If n is less than 1, return an empty string.
def triangle_pattern(n):
    if n < 1:
        return ""
    result = []
    for c in range(1, n+1):
        result.append("*" * c)
    final = "\n".join(result)
    return final  