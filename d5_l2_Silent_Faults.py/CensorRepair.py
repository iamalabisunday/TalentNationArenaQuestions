"""
Crashes cleared. After mess, Sergeant Kay hands over the harder list: three functions that run without raising anything, but return the wrong value. There is no traceback to read. Look at the code, look at what the tests expect, and find the small mistake that bends the answer.

FAULT 3. The redactor at archives is letting every word through. Filed transmissions come out exactly as they went in. Recruit Idris swears the function does the replacement; reviewers swear it does not. Both are right.

Current code:

    def censor(message, word):
        cleaned = message.replace(word, "[REDACTED]")
        return message

Failing test: censor("enemy at the gate", "enemy") returns "enemy at the gate", but archives expect "[REDACTED] at the gate".

"The replacement is being computed and then discarded. The function uses two names that look almost the same. Read the last line carefully and send back the one that holds the cleaned text.
"""
def censor(message, word):
    cleaned = message.replace(word, "[REDACTED]")
    return cleaned