"""
Mid-morning, Sergeant Kay posts the permanent buddy assignments. These are fixed for the rest of the exercise: once assigned, a buddy pair does not change. The right data structure for a fixed record is a tuple: it is created like a list but with round brackets, and Python will not let you change it in place. Today you build and read tuples for grid coordinates, patrol records, and bounding boxes.

TASK 1. A position on the patrol grid is always two numbers: the row and the column. A tuple is the right shape because neither value should change once it is recorded. Implement grid_position(row, col) and return the two values packed into a tuple.

For row 3 and col 7 the answer is (3, 7). A tuple is written with round brackets, or returned as a comma-separated pair without brackets: Python creates the tuple either way.
"""
def grid_position(row, col):
    return [row, col]