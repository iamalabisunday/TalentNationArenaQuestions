"""
Day Four of Operation Watchpoint. The section comes off patrol and files into the operations tent. The intel ledger is a dictionary: every callsign maps to a status. Three jobs to get through before the afternoon audit.

JOB 1. The ledger maps callsigns to their last reported status. Implement get_status(ledger, callsign), where ledger is a dict and callsign is a string. Return the status for that callsign. If the callsign is not in the ledger, return the string unknown rather than raising a KeyError. Use the dict .get() method with a default value so a missing key never causes a crash.
"""
def get_status(ledger, callsign):
    if callsign not in ledger:
        return "unknown"
    return ledger[callsign]