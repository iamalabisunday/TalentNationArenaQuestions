"""
Day Four of Operation Watchpoint. The section comes off patrol and files into the operations tent. The intel ledger is a dictionary: every callsign maps to a status. Three jobs to get through before the afternoon audit.

JOB 4. The duty officer wants the most common status. Implement top_status(counts), where counts is a dict mapping status strings to whole-number counts. Return the status with the highest count. If the dict is empty, return the string none. If two statuses share the top count, return the one that comes first alphabetically. Do not use max(). Iterate the dict, tracking the best seen so far.
"""
# def top_status(counts):
#     if not counts:
#         return "none"
        
#     max_status = "none"
#     max_count = -1
    
#     for status, count in counts.items():
#         if count > max_count:
#             max_count = count
#             max_status = status
            
#     return max_status

def top_status(counts):
    if not counts:
        return "none"
    
    # Get the key and value of the very first dictionary entry
    first_key = list(counts.keys())[0]
    
    max_status = first_key
    max_count = counts[first_key]
    
    for status, count in counts.items():
        if count > max_count:
            max_count = count
            max_status = status
            
    return max_status