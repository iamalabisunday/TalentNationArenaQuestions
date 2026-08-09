"""
By the afternoon, two patrols are sweeping adjacent grids. Patterns to draw, formations to set out, and routes to cross-reference. Each task is a loop inside a loop. Think about the outer loop as the row or the first patrol; the inner loop walks one row's columns or the second patrol's route. Newlines belong between rows, not after the last one.

JOB 1. The grid is rows of asterisks separated by newlines. Implement draw_grid(rows, cols) and return a string with rows lines, each one made of cols asterisks. Lines are separated by a single newline character; there is no trailing newline after the last line.

For 2 rows and 3 columns the answer is ***\n*** as one string. If either rows or cols is 0 or negative, the grid is empty: return an empty string.
"""
def draw_grid(rows, cols):
    if rows <= 0 or cols <= 0:
        return ""
    
    row_str = "*" * cols
    grid = []

    for _ in range(rows):
        grid.append(row_str)
        
    return "\n".join(grid)