"""
Mid-morning. Two patrol logs have come in. Before the full audit, Sergeant Kay wants four quick questions answered using set operations: which callsigns are unique, does any log have duplicates, which callsigns appeared on both patrols, and which appeared only on the first. Sets handle all four in one step each.

TASK 1. The raw log is a list of callsign strings and may contain duplicates. Implement unique_callsigns(log) and return a sorted list containing each callsign exactly once. Convert the list to a set to remove duplicates in one step, then pass the result to sorted() to get a stable, ordered output.

For [Ada, Tunde, Ada] the result is [Ada, Tunde].
"""
def unique_callsigns(log):
    return sorted(set(log))