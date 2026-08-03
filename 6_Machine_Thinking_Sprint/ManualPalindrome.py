# Implement manual_palindrome(text). Ignore spaces and letter case. Return true if the cleaned text reads the same forward and backward, otherwise return false. Do not use slicing shorthand or reversed. Students may need to research manual string reversal.

def manual_palindrome(text):
    forward = ""
    for char in text.lower():
        if char != " ":
            forward += char

    bkd = []
    for i in range(len(forward), 0, -1):
        bkd.append(forward[i-1])

    backward = "".join(bkd)

    return forward == backward