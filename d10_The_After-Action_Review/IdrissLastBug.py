""""
Operation Watchpoint is over. The cohort reassembles in the briefing tent, still smelling of field rations and bad decisions. Sergeant Kay stands at the front, clipboard in one hand, red pen in the other. The After-Action Review covers every section of the exercise. Seven items on the board.

Some of these tasks use tools you have not been taught yet. That is intentional. Part of the review is researching what you need when the lesson has not handed it to you. The instructions will tell you exactly what to look up.

ITEM 6. This is the one the whole exercise has been building towards. Recruit Idris's checkpoint screening code has been rewritten to use the Week 2 toolkit: a list of visitor dicts, a rules dict mapping pass prefixes to actions, and guard clauses with continue. It is cleaner than his Day 6 nested version. But it has one last bug, and it is the same category of mistake he has been making all exercise.

Current code:

    def screen_visitor_v2(visitors, rules):
        results = []
        for visitor in visitors:
            name = visitor.get("name", "")
            code = visitor.get("pass", "")
            escort = visitor.get("escort", False)
            if not name:
                results.append("no name")
                continue
            if not code:
                results.append("no pass")
                continue
            prefix = code[0]
            action = rules.get(prefix, "admit")
            if action == "deny":
                results.append("deny")
            elif action == "escort":
                results.append("needs escort")
            else:
                results.append("admit")
        return results

The rules dict maps a prefix letter to an action: deny means reject outright; escort means they need an escort to be admitted. If the escort field is True and the action is escort, the visitor should be admitted. The current code treats every escort-action visitor as needing an escort, even when they already have one.

Find and fix the bug. The repair is a small change to the elif branch. When the action is escort and the visitor has an escort, the result should be admit. When the action is escort and the visitor does not have an escort, the result should be needs escort.

(When told about this bug, Idris replied: I tested it with a visitor who had no escort and it worked perfectly. Sergeant Kay has requested that quote be engraved on a plaque for the operations tent.)
"""

def screen_visitor_v2(visitors, rules):
    results = []
    for visitor in visitors:
        name = visitor.get("name", "")
        code = visitor.get("pass", "")
        escort = visitor.get("escort", False)
        if not name:
            results.append("no name")
            continue
        if not code:
            results.append("no pass")
            continue
        prefix = code[0]
        action = rules.get(prefix, "admit")
        if action == "deny":
            results.append("deny")
        elif action == "escort":
            results.append("admit" if escort else "needs escort")
        else:
            results.append("admit")
    return results