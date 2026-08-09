"""
Day Three of Operation Watchpoint. The cohort reassembles after the overnight patrols. Sergeant Kay calls morning roll and the roster board needs updating: one recruit has joined from a reserve section, another has been swapped out of a post, and one is standing down for the day. Then the patrol order rotates so yesterday's point scout becomes last in the column. The roster is a list. Lists are mutable: you can change them in place. The functions today receive a list and return the same list after modifying it.

TASK 4. The patrol order rotates. The recruit currently at the front of the column moves to the back. Implement rotate_roster(roster) and return a new list where the first element has moved to the end. All other positions shift one place forward. The original roster must not be changed.

For [Ada, Tunde, Halima] the result is [Tunde, Halima, Ada]. For a roster of zero or one member, the rotation changes nothing. Use slicing to build the new list.
"""
def rotate_roster(roster):
    if not roster:
        return roster
    return roster[1:] + [roster[0]]