# Implement group_by_first_letter(names). Return a dictionary where each key is the uppercase first letter of a name and each value is a list of names that start with that letter. Ignore empty names after stripping spaces. Preserve the order of names inside each group.
def group_by_first_letter(names):
    group = {}
    for name in sorted(names, key=str.lower):
        first_letter = name[0].upper()
        if first_letter not in group:
            group[first_letter] = []
        group[first_letter].append(name)
    return group