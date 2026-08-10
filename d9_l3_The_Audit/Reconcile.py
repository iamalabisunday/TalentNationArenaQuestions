"""
Afternoon. The full intel ledger has been loaded. Sergeant Kay clears the tent and posts your section on the audit. Three tasks, all involving iterating over the ledger or the raw log.

While running Task 2, you find it: Idris's callsign appears twice in the raw patrol log from Day Three, and his two entries map to different statuses in the ledger. Sergeant Kay takes the finding, marks it in the after-action record, and tells you the formal review will happen tomorrow. For tonight, the ledger stands as-is.

TASK 3. After the audit, file a reconciled record. Walk the raw log and for each callsign build a result dict. If the callsign is in the ledger, its value is the ledger status. If it is not, its value is the string unregistered. Implement reconcile(raw_log, ledger). Because the raw log may have duplicates, and a dict key is unique, a callsign that appears twice will simply overwrite its own entry and cause no harm.

For raw_log [Ada, Ghost] and ledger {Ada: active} the result is {Ada: active, Ghost: unregistered}.
"""
def reconcile(raw_log, ledger):
    result = {}
    for callsign in raw_log:
        result[callsign] = ledger.get(callsign, "unregistered")
    return result