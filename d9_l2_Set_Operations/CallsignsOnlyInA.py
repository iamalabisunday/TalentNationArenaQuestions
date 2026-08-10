"""
Mid-morning. Two patrol logs have come in. Before the full audit, Sergeant Kay wants four quick questions answered using set operations: which callsigns are unique, does any log have duplicates, which callsigns appeared on both patrols, and which appeared only on the first. Sets handle all four in one step each.

TASK 4. Find every callsign that appeared on patrol A but not on patrol B. These are the recruits who need a separate debrief. Implement callsigns_only_in_a(patrol_a, patrol_b) and return a sorted list. Convert both lists to sets, use the difference operator -, then sort. The set difference operator - removes from the left set everything that appears in the right set.
"""
def callsigns_only_in_a(patrol_a, patrol_b):
    result = []
    for x in patrol_a:
        if x not in patrol_b:
            result.append(x)
    return sorted(set(result))