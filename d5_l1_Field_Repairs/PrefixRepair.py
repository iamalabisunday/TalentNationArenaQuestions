"""
Before Week 2 you stand on a Field Engineering Detail. Sergeant Kay hands you a clipboard: three pieces of kit have been throwing errors all morning. Read each traceback. The line at the bottom names the fault and points to the line where it happened. Make the smallest change that removes the error and keeps the original behaviour.

FAULT 2. Recruit Chika in signals reads three letters off the front of each callsign. The code worked all week, then a recruit with a two-letter callsign joined this morning and the system crashed.

Current code:

    def prefix_code(callsign):
        return callsign[0] + callsign[1] + callsign[2]

Traceback when called with prefix_code("AB"):

    IndexError: string index out of range

The fault is that the code reads position 2 of a string that only has positions 0 and 1. A slice takes whatever is there without raising; an index read does not. Repair the function so it returns the first three characters when they exist, and whatever shorter string is there when they do not.
"""
def prefix_code(callsign):
    return callsign[0:3]