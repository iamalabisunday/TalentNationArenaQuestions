# Implement reverse_string(value) without using slicing shorthand like [::-1]. Return a new string containing the input characters in reverse order.
def reverse_string(value):
    reverse_char = []
    for char in range(len(value), 0, -1):
        result = value[char-1]
        reverse_char.append(result)
    finalValue = "".join(reverse_char)
    return finalValue