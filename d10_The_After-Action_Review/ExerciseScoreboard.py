"""
Operation Watchpoint is over. The cohort reassembles in the briefing tent, still smelling of field rations and bad decisions. Sergeant Kay stands at the front, clipboard in one hand, red pen in the other. The After-Action Review covers every section of the exercise. Seven items on the board.

Some of these tasks use tools you have not been taught yet. That is intentional. Part of the review is researching what you need when the lesson has not handed it to you. The instructions will tell you exactly what to look up.

ITEM 7. Final item. The exercise is scored. Sergeant Kay reads out the raw results: a list of two-element lists, each one a name and a score from one task. A recruit may appear more than once because they scored on multiple tasks. Implement exercise_scoreboard(records) and return a single string: the scoreboard.

First, aggregate each recruit's scores into a total. Use a dict and .get() to accumulate. Then rank the recruits by total score from highest to lowest. If two recruits share a total, the one whose name comes first alphabetically ranks higher. Finally, build the scoreboard as a multi-line string. Each line is the rank number, a full stop, a space, the name, a space, then the total in round brackets. Lines are joined with newlines; no trailing newline.

For records [[Ada, 10], [Tunde, 8], [Ada, 5]] the scoreboard is:
1. Ada (15)
2. Tunde (8)

You will need to sort a list of two-element pairs by a custom rule. Research the key argument to sorted(). A key function that returns a tuple of the negative score and the name will sort by score descending, then by name ascending.

For an empty list of records, return an empty string.

(Idris asked whether debugging points count. Kay said they do, but only if the bug was not yours to begin with.)
"""
def exercise_scoreboard(records):
    if not records:
        return ""
    
    # 1. Aggregate total scores per recruit using a dictionary
    totals = {}
    for name, score in records:
        totals[name] = totals.get(name, 0) + score
        
    # 2. Sort recruits: score descending (-score), then name ascending (alphabetical)
    # totals.items() gives tuples of (name, total_score)
    ranked = sorted(totals.items(), key=lambda item: (-item[1], item[0]))
    
    # 3. Format into output lines with 1-based rank numbering
    scoreboard_lines = [
        f"{rank}. {name} ({score})" 
        for rank, (name, score) in enumerate(ranked, start=1)
    ]
    
    # 4. Join with newlines (no trailing newline)
    return "\n".join(scoreboard_lines)