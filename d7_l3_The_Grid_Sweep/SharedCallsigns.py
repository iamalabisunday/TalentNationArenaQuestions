"""
By the afternoon, two patrols are sweeping adjacent grids. Patterns to draw, formations to set out, and routes to cross-reference. Each task is a loop inside a loop. Think about the outer loop as the row or the first patrol; the inner loop walks one row's columns or the second patrol's route. Newlines belong between rows, not after the last one.

JOB 3. Two patrols compare rosters. For each callsign character in roster A, count it if the same character appears anywhere in roster B. Each position in roster A counts at most once, even if the matching character appears more than once in roster B. Implement shared_callsigns(roster_a, roster_b) with a loop over A around a loop over B, and use break in the inner loop to avoid double-counting.

For roster A ABBA and roster B B the answer is 2: A does not appear in B; the first B in A counts; the second B in A counts; the second A does not. For an empty roster the answer is 0.

Lists arrive tomorrow; today both rosters are strings.
"""
def shared_callsigns(roster_a, roster_b):
    if roster_a == "" or roster_b == "":
        return 0
    count = 0
    for count_a in roster_a:
        for count_b in roster_b:
            if count_a == count_b:
                count += 1
                break
    return count