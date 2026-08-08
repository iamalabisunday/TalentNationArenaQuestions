"""
After mess, your section relieves Recruit Idris at the side checkpoint. His last shift ended badly: a visitor with a pass that needed an escort walked through, because his screening was tangled in nested if/else and missed the case. The duty officer wants the checkpoint rewritten tonight, using guard clauses.

The pattern is straightforward. Each bad case is returned early, in order; the happy path sits at the bottom with nothing nested around it. Read top-to-bottom, the function says: rule out this; rule out this; rule out this; otherwise, proceed.

TASK 1. Before any visitor is screened, the pass itself must be sound. Implement validate_pass(pass_code) using guard clauses, returning early for each bad case in this order:

    empty pass                -> "no pass"
    shorter than 5 characters -> "too short"
    does not start with "P"   -> "invalid prefix"
    otherwise                 -> "valid"

The order matters: the empty case must be ruled out first, because the length and prefix checks would otherwise mishandle it.
"""
def validate_pass(pass_code):
    if pass_code == "":
        return "no pass"
    elif len(pass_code) < 5:
        return "too short"
    elif pass_code[0].lower() == "p":
        return "invalid"
    else:
        return "valid prefix"