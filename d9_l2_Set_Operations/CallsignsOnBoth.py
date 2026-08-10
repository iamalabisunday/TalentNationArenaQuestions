"""
Mid-morning. Two patrol logs have come in. Before the full audit, Sergeant Kay wants four quick questions answered using set operations: which callsigns are unique, does any log have duplicates, which callsigns appeared on both patrols, and which appeared only on the first. Sets handle all four in one step each.

TASK 3. Find every callsign that appeared on both patrols. Implement callsigns_on_both(patrol_a, patrol_b), where each argument is a list of strings. Return a sorted list of callsigns present in both. Convert both lists to sets and use the intersection operator & to find common elements, then sort the result for stable output.
"""
def callsigns_on_both(patrol_a, patrol_b):
    result = []
    for x in patrol_a:
        if x in patrol_b:
            result.append(x)
    return sorted(set(result))