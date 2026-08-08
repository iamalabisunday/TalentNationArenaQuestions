"""
Relieved at the gate by Recruit Idris's section, you climb to the watchtower for the second watch. Three readings feed into each decision. Today the lesson is how to combine them with and, or, and not, and where the brackets must go.

READING 3. The tower runs a tiered alert. Implement threat_level(motion, thermal, weapon) returning one of four words. The rules are checked in this order:

    weapon detected            -> critical
    both motion AND thermal     -> high
    motion OR thermal (just one) -> medium
    nothing                    -> clear

The first rule that fits decides the answer. A weapon trumps everything; both sensors together are worse than one alone. Combine Boolean logic from this lesson with the if-elif-else chain from Lesson 1.
"""
def threat_level(motion, thermal, weapon):
    if weapon is True:
        return "critical"
    elif motion and thermal is True:
        return "high"
    elif motion or thermal is True:
        return "medium"
    else:
        return "clear"