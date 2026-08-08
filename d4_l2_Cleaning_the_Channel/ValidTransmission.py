"""
A transmission is well formed only if it starts with BEGIN, ends with END, and contains the separator // somewhere in between. Implement is_valid_transmission(message) and return True when all three hold, and False otherwise. Use the string methods for the start and end, the in operator for the separator, and the and operator to join the three checks.
"""
def is_valid_transmission(message):
    return (
        message.startswith("BEGIN") 
        and message.endswith("END") 
        and "//" in message
    )