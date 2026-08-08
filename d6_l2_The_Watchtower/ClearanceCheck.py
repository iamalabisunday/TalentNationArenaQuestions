"""
Relieved at the gate by Recruit Idris's section, you climb to the watchtower for the second watch. Three readings feed into each decision. Today the lesson is how to combine them with and, or, and not, and where the brackets must go.

READING 2. Visitors only clear the tower's check when every safety rule holds: identity verified AND not on the watchlist AND they either have an escort OR carry a senior pass. The escort and the senior pass are alternatives; everything else is required.

Implement can_clear(identity_ok, not_flagged, has_escort, senior_pass) and return True or False. The brackets around the OR are the whole point of this exercise: without them, the expression means something different. Return the expression directly.
"""
def can_clear(identity_ok, not_flagged, has_escort, senior_pass):
    return identity_ok and not_flagged and (has_escort or senior_pass)