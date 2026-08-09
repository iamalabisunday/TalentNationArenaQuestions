"""
Day Three of Operation Watchpoint. The cohort reassembles after the overnight patrols. Sergeant Kay calls morning roll and the roster board needs updating: one recruit has joined from a reserve section, another has been swapped out of a post, and one is standing down for the day. Then the patrol order rotates so yesterday's point scout becomes last in the column. The roster is a list. Lists are mutable: you can change them in place. The functions today receive a list and return the same list after modifying it.

TASK 2. A recruit at a given position is being swapped. Implement replace_recruit(roster, index, name). Assign name to roster at index and return the roster. Do not create a new list. You can assume the index is always valid.

For roster [Ada, Tunde, Halima], index 1, and name Chika the result is [Ada, Chika, Halima].
"""
def replace_recruit(roster, index, name):
    roster[index] = name
    return roster