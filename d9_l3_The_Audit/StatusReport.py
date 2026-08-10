"""
Afternoon. The full intel ledger has been loaded. Sergeant Kay clears the tent and posts your section on the audit. Three tasks, all involving iterating over the ledger or the raw log.

While running Task 2, you find it: Idris's callsign appears twice in the raw patrol log from Day Three, and his two entries map to different statuses in the ledger. Sergeant Kay takes the finding, marks it in the after-action record, and tells you the formal review will happen tomorrow. For tonight, the ledger stands as-is.

TASK 1. Print a sorted report of every callsign and its status. Implement status_report(ledger), where ledger is a dict. Return a single string containing one line per entry in alphabetical order by callsign. Each line is the callsign, a colon, a space, then the status. Lines are joined with newlines; no trailing newline.

For {Tunde: standby, Ada: active} the result is:
Ada: active
Tunde: standby
"""
def status_report(ledger):
    lines = []
    for callsign in sorted(ledger):
        lines.append(f"{callsign}: {ledger[callsign]}")
    return "\n".join(lines)