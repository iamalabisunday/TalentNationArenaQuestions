"""
Mid-morning, Sergeant Kay posts the permanent buddy assignments. These are fixed for the rest of the exercise: once assigned, a buddy pair does not change. The right data structure for a fixed record is a tuple: it is created like a list but with round brackets, and Python will not let you change it in place. Today you build and read tuples for grid coordinates, patrol records, and bounding boxes.

TASK 2. After the patrol, the duty officer wants to know the bounding box of all positions visited: the minimum row, the maximum row, the minimum column, and the maximum column. Implement patrol_bounds(positions), where positions is a list of (row, col) tuples, and return a single tuple of four values in this order: min row, max row, min col, max col.

For [(1, 3), (4, 1), (2, 5)] the answer is (1, 4, 1, 5). You may use min() and max() with a list comprehension to extract each coordinate axis, or walk the list with a loop. A list comprehension that reads p[0] for p in positions gives all the row values.
"""
def patrol_bounds(positions):
    rows = [p[0] for p in positions]
    cols = [p[1] for p in positions]
    return [min(rows), max(rows), min(cols), max(cols)]

# def patrol_bounds(positions):
#     min_row, max_row = positions[0][0], positions[0][0]
#     min_col, max_col = positions[0][1], positions[0][1]
    
#     for row, col in positions:
#         if row < min_row:
#             min_row = row
#         if row > max_row:
#             max_row = row
#         if col < min_col:
#             min_col = col
#         if col > max_col:
#             max_col = col
            
#     return (min_row, max_row, min_col, max_col)