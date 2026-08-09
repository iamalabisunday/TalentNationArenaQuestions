"""
Late afternoon. The raw patrol log has come in and it is messy: blank entries, names with stray spaces and wrong capitalisation, and more names than there should be. The duty clerk asks your section to clean it up before it goes to archive. Yesterday you did this with for loops; today the lesson is to compress that into a list comprehension. While running the filter, you notice that Recruit Idris's callsign appears twice in the log. You flag it to Sergeant Kay, who says to leave it for now: it will be audited tomorrow when the full intel ledger is reconciled.

TASK 2. Some names have stray spaces and inconsistent capitalisation. Implement normalised_roster(roster), where roster is a list of strings, and return a new list where every name has been stripped of surrounding spaces and converted to title case. Include every name, even blank entries (a blank stripped is still blank). Use a list comprehension with a transformation expression.

For [  ada  ,  tunde idris] the result is [Ada, Tunde Idris]. Title case capitalises the first letter of each word.
"""
def normalised_roster(roster):
    result = []
    for char in roster:
        p = char.strip().title()
        result.append(p)
    return result