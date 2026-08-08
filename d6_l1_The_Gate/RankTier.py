"""
Night one of Operation Watchpoint. Your section takes the main gate from twenty hundred. Three visitor decisions land in front of you in turn, each a little harder than the last. Use if, elif, and else; do not stack separate if statements where one elif chain belongs.

POST 2. The pass system also reads a rank number on the back of each card. Implement rank_tier(rank), where rank is a whole number, and return the access tier:

    1       -> general access
    2 or 3  -> restricted
    4 or 5  -> command
    anything else -> invalid rank

Ranks 2 and 3 share a tier and so do 4 and 5; combine them in a single elif branch with the or operator rather than writing two near-identical branches.
"""
def rank_tier(rank):
    rank = int(rank)
    if rank == 1:
        return "general access"
    elif rank == 2 or rank == 3:
        return "restricted"
    elif rank == 4 or rank == 5:
        return "command"
    else:
        return "invalid rank"