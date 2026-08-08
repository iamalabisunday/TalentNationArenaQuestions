"""
Crashes cleared. After mess, Sergeant Kay hands over the harder list: three functions that run without raising anything, but return the wrong value. There is no traceback to read. Look at the code, look at what the tests expect, and find the small mistake that bends the answer.

FAULT 1. The reversing code for intercepted signals returns each signal unchanged. No error, just the wrong answer.

Current code:

    def reverse_signal(message):
        return message[::1]

Failing test: reverse_signal("ALPHA") returns "ALPHA", but the report expects "AHPLA".

The slice is the right shape but one number is wrong. Read the slice carefully: a step of plus one walks the string forwards, which is why nothing changes. Pick the step that walks it backwards.
"""
def reverse_signal(message):
    return message[::-1]
