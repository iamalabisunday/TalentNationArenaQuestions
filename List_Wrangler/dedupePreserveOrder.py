# Implement dedupe_preserve_order(items). Return a new list with duplicate values removed while keeping the first time each value appeared. Do not use set for this challenge.
def dedupe_preserve_order(items):
    seen = []
    result = []
    for n in items:
        if n not in seen:
            seen.append(n)
            result.append(n)
    return result