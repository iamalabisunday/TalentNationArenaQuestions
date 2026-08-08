"""
After mess, your section relieves Recruit Idris at the side checkpoint. His last shift ended badly: a visitor with a pass that needed an escort walked through, because his screening was tangled in nested if/else and missed the case. The duty officer wants the checkpoint rewritten tonight, using guard clauses.

The pattern is straightforward. Each bad case is returned early, in order; the happy path sits at the bottom with nothing nested around it. Read top-to-bottom, the function says: rule out this; rule out this; rule out this; otherwise, proceed.

TASK 3. This is the one Idris got wrong last week. A visitor's pass begins with one of two prefixes that change the rules:

    pass starts with "X" -> banned, deny outright
    pass starts with "R" -> restricted, needs an escort

Implement screen_visitor(name, pass_code, escort), where escort is a Boolean, with these guards in order:

    empty name                                   -> "no name"
    empty pass                                   -> "no pass"
    pass starts with "X"                          -> "deny"
    pass starts with "R" and no escort present    -> "needs escort"
    otherwise                                    -> "admit"

The order matters. The X check has to come before the R check, because an X pass is denied even with an escort. A visitor with an R pass and an escort is admitted; without an escort, they are turned back. Read the function top-to-bottom: each bad case returns early, then admit.
"""
def screen_visitor(name, pass_code, escort):
    if name == "":
        return "no name"
    elif pass_code == "":
        return "no pass"
    elif pass_code[0].lower() == "x":
        return "deny"
    elif pass_code[0].lower() == "r":
        if not escort:
            return "needs escort"
        else:
            return "admit"
    else:
        return "admit"