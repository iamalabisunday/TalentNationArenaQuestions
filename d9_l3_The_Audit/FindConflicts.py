"""
Afternoon. The full intel ledger has been loaded. Sergeant Kay clears the tent and posts your section on the audit. Three tasks, all involving iterating over the ledger or the raw log.

While running Task 2, you find it: Idris's callsign appears twice in the raw patrol log from Day Three, and his two entries map to different statuses in the ledger. Sergeant Kay takes the finding, marks it in the after-action record, and tells you the formal review will happen tomorrow. For tonight, the ledger stands as-is.

TASK 2. This is the audit. A conflict is a callsign that appears more than once in the raw log AND is present in the ledger. Implement find_conflicts(raw_log, ledger), where raw_log is a list of callsign strings and ledger is a dict. Return a sorted list of conflicting callsigns, with each name appearing once regardless of how many times it repeats.

Walk the log with a loop. Track which callsigns you have seen so far in a set. When you see a callsign that is already in the seen set and is also a key in the ledger, it is a conflict. Idris's callsign will appear here.

For raw_log [Ada, Idris, Ada, Idris] and ledger {Ada: active, Idris: standby} the result is [Ada, Idris].
"""
def find_conflicts(raw_log, ledger):
    seen = set()
    conflicts = set()
    
    for callsign in raw_log:
        if callsign in seen and callsign in ledger:
            conflicts.add(callsign)
        seen.add(callsign)
        
    return sorted(conflicts)