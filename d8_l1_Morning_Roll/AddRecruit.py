"""
Day Three of Operation Watchpoint. The cohort reassembles after the overnight patrols. Sergeant Kay calls morning roll and the roster board needs updating: one recruit has joined from a reserve section, another has been swapped out of a post, and one is standing down for the day. Then the patrol order rotates so yesterday's point scout becomes last in the column. The roster is a list. Lists are mutable: you can change them in place. The functions today receive a list and return the same list after modifying it.

TASK 1. A new recruit has arrived from reserve. Implement add_recruit(roster, name). Add name to the end of the roster and return the roster. Do not create a new list; modify the one that was passed in using .append() and return it.

For roster [Ada, Tunde] and name Halima the result is [Ada, Tunde, Halima].
"""
def add_recruit(roster, name):
    roster.append(name)
    return roster