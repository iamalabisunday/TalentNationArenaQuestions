"""
After mess, your section relieves Recruit Idris at the side checkpoint. His last shift ended badly: a visitor with a pass that needed an escort walked through, because his screening was tangled in nested if/else and missed the case. The duty officer wants the checkpoint rewritten tonight, using guard clauses.

The pattern is straightforward. Each bad case is returned early, in order; the happy path sits at the bottom with nothing nested around it. Read top-to-bottom, the function says: rule out this; rule out this; rule out this; otherwise, proceed.

TASK 2. The quartermaster sends incoming requisitions to the checkpoint for clearance. Implement process_requisition(item, quantity) using guard clauses, returning early for each bad case:

    empty item                -> "missing item"
    quantity is 0 or negative -> "invalid quantity"
    quantity is over 100      -> "exceeds limit"
    otherwise                 -> the line approved: Q x I where Q is the quantity and I is the item.

For ("rifle", 5) the approval reads approved: 5 x rifle.
"""
def process_requisition(item, quantity):
    quantity = int(quantity)
    if item == "":
        return "missing item"
    elif quantity <= 0:
        return "invalid quantity"
    elif quantity > 100:
        return "exceeds limit"
    else:
        return f"approved: {quantity} x {item}"