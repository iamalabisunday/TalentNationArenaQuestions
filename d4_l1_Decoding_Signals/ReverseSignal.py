"""
An intercepted signal arrives back to front. Implement reverse_signal(message) and return the message reversed. The canonical way to reverse a string in Python is the slice with a step of minus one. Do not use reversed(). An empty message reverses to an empty message.
"""
def reverse_signal(message):
    return str(message)[::-1]