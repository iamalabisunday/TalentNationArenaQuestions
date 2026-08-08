"""
Crashes cleared. After mess, Sergeant Kay hands over the harder list: three functions that run without raising anything, but return the wrong value. There is no traceback to read. Look at the code, look at what the tests expect, and find the small mistake that bends the answer.

FAULT 2. The range scoreboard has been overstating scores all week. Recruits with bad shoots have been posting suspiciously high numbers. Five points per hit, two points lost per miss is the rule; the code treats the miss penalty as a reward.

Current code:

    def range_score(hits, misses):
        return hits * 5 + misses * 2

Failing test: range_score(10, 2) returns 54, but the rulebook expects 46.

The two multiplications are correct. Only the operator joining them is wrong. Pick the operator that takes the miss penalty away.
"""
def range_score(hits, misses):
    res_1 = hits * 5
    res_2 = misses * 2
    return res_1 - res_2