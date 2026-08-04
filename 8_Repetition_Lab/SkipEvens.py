# Implement skip_evens(start, end). Return a list of odd numbers from start to end inclusive. Use continue to skip even numbers. If start is greater than end, return an empty list.
def skip_evens(start, end):
    if start > end:
        return []
    result = []
    for num in range(start, end+1):
        if num % 2 == 0:
            continue
        else:
            result.append(num)
    return result