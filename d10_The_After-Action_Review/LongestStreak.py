"""
Operation Watchpoint is over. The cohort reassembles in the briefing tent, still smelling of field rations and bad decisions. Sergeant Kay stands at the front, clipboard in one hand, red pen in the other. The After-Action Review covers every section of the exercise. Seven items on the board.

Some of these tasks use tools you have not been taught yet. That is intentional. Part of the review is researching what you need when the lesson has not handed it to you. The instructions will tell you exactly what to look up.

ITEM 2. The patrol log is a list of status strings recorded at each checkpoint. The duty officer wants to know the longest consecutive run of the same status. Implement longest_streak(log) and return the length of the longest streak.

Walk the list with an index. Track two things: the current run length and the best run length seen so far. When the current status matches the previous one, the run grows. When it does not, the run resets to one. Do not use max(); track the best inside the loop.

For [clear, clear, clear, alert, clear] the longest streak is 3. For an empty log the answer is 0. For a log with one entry the answer is 1. (Idris holds the exercise record for consecutive clear readings. He also holds the record for false negatives, but we are not scoring that today.)
"""
def longest_streak(log):
    if len(log) == 0:
        return 0

    current_streak = 1
    longest = 1

    for i in range(1, len(log)):
        if log[i] == log[i-1]:
            current_streak += 1
            if current_streak > longest:
                longest = current_streak
        else:
            current_streak = 1

    return longest