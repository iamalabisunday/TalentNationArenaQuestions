"""
Day Three of Operation Watchpoint. The cohort reassembles after the overnight patrols. Sergeant Kay calls morning roll and the roster board needs updating: one recruit has joined from a reserve section, another has been swapped out of a post, and one is standing down for the day. Then the patrol order rotates so yesterday's point scout becomes last in the column. The roster is a list. Lists are mutable: you can change them in place. The functions today receive a list and return the same list after modifying it.

TASK 3. A recruit is standing down. Implement remove_recruit(roster, name). If name is in the roster, remove the first occurrence and return the roster. If name is not in the roster, return the roster unchanged. Do not raise an error for a missing name.
"""
def remove_recruit(roster, name):
    if name in roster:
        roster.remove(name)
    return roster