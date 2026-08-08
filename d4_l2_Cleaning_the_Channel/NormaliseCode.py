"""
Codes arrive messy and must be cleaned before they can be matched. Implement normalise_code(raw) and return the code with the surrounding spaces trimmed, all letters in lower case, and every remaining space removed. Methods return new strings, so you can chain them in one line: trim, then lower, then remove spaces. The code AL PHA with stray spaces becomes alpha.
"""
def normalise_code(raw):
    word = raw.strip().lower().replace(" ","")
    return word