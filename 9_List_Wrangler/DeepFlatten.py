# Implement deep_flatten(items). Return a flat list containing every non-list value from items, no matter how deeply nested the lists are. Students may need to research recursion. Preserve the left-to-right order.
def deep_flatten(items):
    flat_list = []
    for item in items:
        if isinstance(item, list):
            # Recursively flatten sublists and extend the result
            flat_list.extend(deep_flatten(item))
        else:
            # Append non-list items directly
            flat_list.append(item)
    return flat_list