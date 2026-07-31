# Implement skip_evens(start, end). Return a list of odd numbers from start to end inclusive. Use continue to skip even numbers. If start is greater than end, return an empty list.

def skip_evens(start, end):
    result = []
    for n in range(start, end + 1):
        if int(n) % 2 != 0:
            result.append(n)
    return result