"""
Dawn patrol on Day Two of Operation Watchpoint. Your section steps off into the perimeter sweep at oh-six-hundred. Three jobs across the morning, each one a small for loop. Today is the day the loop stops being a spelling and starts being a tool.

JOB 1. The patrol is broken into legs. Leg one is 1 pace, leg two is 2 paces, leg three is 3 paces, and so on. Implement total_paces(n) and return the total number of paces after the first n legs. Build the total with a for loop over range; do not use sum().

For n = 3 the total is 1 + 2 + 3 = 6. For n = 0 the patrol has not stepped off, so the total is 0.
"""

def total_paces(n):
    if n == 0:
        return 0

    count = 0
    for c in range(1, n+1):
        count += c
    return count