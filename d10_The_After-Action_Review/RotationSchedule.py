"""
Operation Watchpoint is over. The cohort reassembles in the briefing tent, still smelling of field rations and bad decisions. Sergeant Kay stands at the front, clipboard in one hand, red pen in the other. The After-Action Review covers every section of the exercise. Seven items on the board.

Some of these tasks use tools you have not been taught yet. That is intentional. Part of the review is researching what you need when the lesson has not handed it to you. The instructions will tell you exactly what to look up.

ITEM 5. The duty officer wants a rotation table. Given a roster of names and a number of shifts, produce a list of lists. Shift 0 is the original order. Shift 1 rotates every position forward by one, so the recruit who was second is now first, and the one who was first wraps to the end. Shift 2 rotates by two, and so on.

Implement rotation_schedule(roster, shifts). For each shift s, build a new list where the recruit at position i in the original roster moves to the position (i + s) mod length. The modulo handles the wrap. Return a list of shifts lists.

For roster [Ada, Tunde, Halima] and 3 shifts the result is:
  [[Ada, Tunde, Halima],
   [Tunde, Halima, Ada],
   [Halima, Ada, Tunde]]

(Idris asked whether he could be permanently assigned to Shift 0. Kay said no.)
"""

def rotation_schedule(roster: list[str], shifts: int) -> list[list[str]]:
    if not roster:
        return [[] for _ in range(shifts)]
    
    schedule = []
    n = len(roster)
    
    for s in range(shifts):
        effective_shift = s % n
        shifted_roster = roster[effective_shift:] + roster[:effective_shift]
        schedule.append(shifted_roster)
        
    return schedule