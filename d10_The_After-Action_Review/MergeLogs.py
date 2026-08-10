"""
Operation Watchpoint is over. The cohort reassembles in the briefing tent, still smelling of field rations and bad decisions. Sergeant Kay stands at the front, clipboard in one hand, red pen in the other. The After-Action Review covers every section of the exercise. Seven items on the board.

Some of these tasks use tools you have not been taught yet. That is intentional. Part of the review is researching what you need when the lesson has not handed it to you. The instructions will tell you exactly what to look up.

ITEM 4. Two patrols filed their logs in time order, but they need to be combined into one sorted timeline. Both inputs are already sorted from lowest to highest. Implement merge_logs(log_a, log_b) and return a single sorted list containing every element from both.

Use two index variables, one for each list. Compare the current elements; whichever is smaller (or equal) goes into the result first, and its index advances. When one list runs out, append everything remaining from the other. This is the merge step of merge sort, and it runs in one pass through both lists.

Do not use sorted() or .sort() on the combined result. The point is to merge efficiently with a while loop, not to concatenate and re-sort.

For [1, 3, 5] and [2, 4, 6] the result is [1, 2, 3, 4, 5, 6]. (The duty clerk attempted this task by piling both stacks of paper together and shuffling. It did not go well.)
"""

def merge_logs(log_a, log_b):
    merged = []
    i = 0  # Pointer for log_a
    j = 0  # Pointer for log_b

    # Compare elements from both lists and append the smaller one
    while i < len(log_a) and j < len(log_b):
        if log_a[i] <= log_b[j]:
            merged.append(log_a[i])
            i += 1
        else:
            merged.append(log_b[j])
            j += 1

    # Append any remaining elements from log_a
    while i < len(log_a):
        merged.append(log_a[i])
        i += 1

    # Append any remaining elements from log_b
    while j < len(log_b):
        merged.append(log_b[j])
        j += 1

    return merged