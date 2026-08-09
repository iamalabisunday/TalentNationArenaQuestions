"""
Late afternoon. The raw patrol log has come in and it is messy: blank entries, names with stray spaces and wrong capitalisation, and more names than there should be. The duty clerk asks your section to clean it up before it goes to archive. Yesterday you did this with for loops; today the lesson is to compress that into a list comprehension. While running the filter, you notice that Recruit Idris's callsign appears twice in the log. You flag it to Sergeant Kay, who says to leave it for now: it will be audited tomorrow when the full intel ledger is reconciled.

TASK 1. The raw roster contains some blank entries where a slot was never filled. Implement active_names(roster), where roster is a list of strings, and return a new list containing only the non-empty strings, in their original order. Use a list comprehension with an if condition. An empty string is the only thing to exclude.

For [Ada, , Tunde, , Halima] the result is [Ada, Tunde, Halima].
"""
def active_names(roster):
    result = []
    for n in roster:
        if n != "":
            result.append(n)
    return result