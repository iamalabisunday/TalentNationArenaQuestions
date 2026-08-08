"""
Transmissions are wrapped in a single marker character at each end. Implement drop_ends(message) and return the message with the first and last characters removed. A slice from index one up to (but not including) the last index does this. Mind the short cases: a message of zero, one, or two characters has nothing left in the middle, so it returns an empty string.
"""
def drop_ends(message):
    last = len(message)-1
    return message[1:last]