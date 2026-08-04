# Implement chunk_list(items, size). Split items into smaller lists of length size. The final chunk may be shorter if there are not enough items left. If size is less than 1, return Invalid size.
def chunk_list(items, size):
    if size < 1:
        return "Invalid size"
    final = [items[i:i + size] for i in range(0, len(items), size)]
    return final

# or 

def chunk_list(items, size):
    if size < 1:
        return "Invalid size"
    result = []
    for i in range(0, len(items), size):
        result.append(items[i:i + size])
    return result