"""
Day Four of Operation Watchpoint. The section comes off patrol and files into the operations tent. The intel ledger is a dictionary: every callsign maps to a status. Three jobs to get through before the afternoon audit.

JOB 3. Two parallel lists have arrived from the field: one of callsigns, one of statuses, in the same order. Implement build_ledger(callsigns, statuses) and return a dict that maps each callsign to its matching status. You can assume both lists are the same length. Use range(len()) to walk both lists by index together.

For callsigns [Ada, Tunde] and statuses [active, standby] the result is {Ada: active, Tunde: standby}.
"""
