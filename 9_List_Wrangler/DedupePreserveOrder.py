# Implement dedupe_preserve_order(items). Return a new list with duplicate values removed while keeping the first time each value appeared. Do not use set for this challenge.
def dedupe_preserve_order(items):
    result = []
    for item in items:
        if item not in result:
            result.append(item)
    return result