"""
Late afternoon. The raw patrol log has come in and it is messy: blank entries, names with stray spaces and wrong capitalisation, and more names than there should be. The duty clerk asks your section to clean it up before it goes to archive. Yesterday you did this with for loops; today the lesson is to compress that into a list comprehension. While running the filter, you notice that Recruit Idris's callsign appears twice in the log. You flag it to Sergeant Kay, who says to leave it for now: it will be audited tomorrow when the full intel ledger is reconciled.

TASK 3. The archive system has a minimum callsign length for formal records. Implement long_names(roster, min_length), where roster is a list of strings and min_length is a whole number. Return a new list containing only the names whose length is at least min_length, in their original order. Use a list comprehension with an if condition on len().

For roster [Ada, Tunde, Halima] and min_length 5 the result is [Tunde, Halima] because Ada has only three characters. If no names qualify, return an empty list.
"""
def long_names(roster, min_length):
    result = []
    for char in roster:
        if len(char) >= min_length:
            result.append(char)
    return result