"""
A transmission must be redacted before it is filed. Implement censor(message, word) and return the message with every occurrence of word replaced by the text [REDACTED] in square brackets. If the word does not appear, return the message unchanged. Be aware that replace works on any matching run of characters, not only whole words.
"""
def censor(message, word):
    mess = message.lower().strip().replace(word, "[REDACTED]")
    return mess