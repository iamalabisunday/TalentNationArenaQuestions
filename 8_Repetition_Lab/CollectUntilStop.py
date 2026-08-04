# Implement collect_until_stop(items). Loop through the list and collect items until an item becomes stop after stripping spaces and converting to lowercase. Return the collected items before stop. Use break when stop is found.
def collect_until_stop(items):
    result = []
    for item in items:
        item_cov = item.strip().lower() 
        if item_cov != "stop":
            result.append(item_cov)
        else:
            break
    return result