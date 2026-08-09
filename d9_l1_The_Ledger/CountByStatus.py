"""
Day Four of Operation Watchpoint. The section comes off patrol and files into the operations tent. The intel ledger is a dictionary: every callsign maps to a status. Three jobs to get through before the afternoon audit.

JOB 2. The duty officer wants a headcount by status. Implement count_by_status(entries), where entries is a list of status strings. Return a dict mapping each distinct status to how many times it appears. Build the counts with a loop and .get() with a default of zero. Do not use collections.Counter.

For [active, standby, active] the result is {active: 2, standby: 1}.
"""
def count_by_status(entries):
    counts = {}
    for status in entries:
        counts[status] = counts.get(status, 0) + 1
    return counts