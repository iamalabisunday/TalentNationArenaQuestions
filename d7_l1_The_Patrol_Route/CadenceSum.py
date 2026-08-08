"""
Dawn patrol on Day Two of Operation Watchpoint. Your section steps off into the perimeter sweep at oh-six-hundred. Three jobs across the morning, each one a small for loop. Today is the day the loop stops being a spelling and starts being a tool.

JOB 3. The lead caller paces a cadence every third step: pace 3, pace 6, pace 9, and on. Implement cadence_sum(n) and return the sum of every third pace from 3 up to and including n. Use range with three arguments: start, stop, and step. Do not use sum().

For n = 9 the sum is 3 + 6 + 9 = 18. For n = 8 the last cadence pace is 6 because 9 is past the end, so the sum is 9. For n less than 3 there is no cadence yet, so the sum is 0.
"""
def cadence_sum(n):
    total = 0
    for pace in range(3, n + 1, 3):
        total += pace
    return total