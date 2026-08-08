"""
Night one of Operation Watchpoint. Your section takes the main gate from twenty hundred. Three visitor decisions land in front of you in turn, each a little harder than the last. Use if, elif, and else; do not stack separate if statements where one elif chain belongs.

POST 3. After twenty-two hundred the gate runs on stricter rules. Implement after_hours_admit(pass_color, hour), where pass_color is the colour from POST 1 and hour is the current hour as a whole number from 0 to 23. Apply this order:

    red    -> deny      (any hour)
    amber  -> hold      (any hour)
    green and the hour is from 6 up to but not including 22
           -> admit
    green at any other hour
           -> admit with escort
    anything else (unknown colour) -> verify

The colour is checked first; the hour only matters for green passes. Use a single if-elif-else chain. The hour range can be written as one chained comparison, as on Day 3.
"""
def after_hours_admit(pass_color, hour):
    hour = int(hour)

    if pass_color == "red":
        return "deny"
    elif pass_color == "amber":
        return "hold"
    elif pass_color == "green":
        if 6 <= hour < 22:
            return "admit" 
        else:
            return "admit with escort"
    else:
        return "verify"