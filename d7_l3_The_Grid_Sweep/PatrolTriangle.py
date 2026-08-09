"""
By the afternoon, two patrols are sweeping adjacent grids. Patterns to draw, formations to set out, and routes to cross-reference. Each task is a loop inside a loop. Think about the outer loop as the row or the first patrol; the inner loop walks one row's columns or the second patrol's route. Newlines belong between rows, not after the last one.

JOB 2. The formation is a right-angled triangle: row 1 is one asterisk, row 2 is two, row 3 is three, on up to row n. Implement patrol_triangle(n) and return a string with n lines separated by newlines, with no trailing newline.

For n = 3 the answer is *\n**\n*** as one string. For n = 0 the formation is empty: return an empty string. The inner loop's length depends on the outer loop's index, which is the point of the exercise.
"""
def patrol_triangle(n):
    if n == 0:
        return ""

    patrol = []
    for c in range(1, n+1):
        star = "*" * c
        patrol.append(star)
    
    return "\n".join(patrol)