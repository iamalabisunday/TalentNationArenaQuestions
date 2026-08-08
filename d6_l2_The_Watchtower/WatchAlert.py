"""
Relieved at the gate by Recruit Idris's section, you climb to the watchtower for the second watch. Three readings feed into each decision. Today the lesson is how to combine them with and, or, and not, and where the brackets must go.

READING 1. The simplest tower rule. Sound the alert only when there is motion AND it is after curfew. Both must hold. Implement watch_alert(motion, after_curfew) and return True or False. Return the Boolean expression directly; you do not need an if statement.
"""
def watch_alert(motion, after_curfew):
    return motion and after_curfew