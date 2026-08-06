"""
A requisition arrives with the round count written as text, for example the string 42. Implement to_rounds(text) and return that count as a whole number so the stores can add it up. The text is always a valid whole number, but it may carry stray spaces around it, and it may be negative.
"""
def to_rounds(text):
    text = int(text)
    return text