"""
Mid-morning. Two patrol logs have come in. Before the full audit, Sergeant Kay wants four quick questions answered using set operations: which callsigns are unique, does any log have duplicates, which callsigns appeared on both patrols, and which appeared only on the first. Sets handle all four in one step each.

TASK 2. Before filing the log, the clerk checks whether any callsign appears more than once. Implement has_duplicates(log) and return True if the log contains any duplicate, and False if every entry is unique. A list and its set version have the same length only when there are no duplicates: comparing the two lengths is the one-line test.
"""
def has_duplicates(log):
    if len(log) != len(sorted(set(log))):
        return True
    else:
        return False