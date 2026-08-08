"""
Before Week 2 you stand on a Field Engineering Detail. Sergeant Kay hands you a clipboard: three pieces of kit have been throwing errors all morning. Read each traceback. The line at the bottom names the fault and points to the line where it happened. Make the smallest change that removes the error and keeps the original behaviour.

FAULT 3. Recruit Halima at the quartermaster's desk has been unable to log a single code today: every call to the cleaning function fails. The code reads almost correctly, but one method does not exist.

Current code:

    def normalise_code(raw):
        return raw.strip().lowercase().replace(" ", "")

Traceback when called with normalise_code("  AL PHA  "):

    AttributeError: 'str' object has no attribute 'lowercase'

An AttributeError on a string means a method was called by a name that Python does not recognise on strings. Look up the correct name for converting text to lower case and replace the misspelled call. The rest of the chain is correct.
"""
def normalise_code(raw):
    return raw.strip().lower().replace(" ", "")