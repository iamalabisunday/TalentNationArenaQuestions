# Implement initials_badge(full_name). Remove leading and trailing spaces, split the name into words, take the first character of each word, convert each initial to uppercase, and return the initials joined with dots. The returned badge should end with a dot.

def initials_badge(full_name):
    clean = full_name.strip().split()
    first_char = []
    for i in clean:
        first_char.append(i[0])
    result = ".".join(first_char) + "."
    return result.upper()