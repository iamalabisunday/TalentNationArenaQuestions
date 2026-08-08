"""
Night one of Operation Watchpoint. Your section takes the main gate from twenty hundred. Three visitor decisions land in front of you in turn, each a little harder than the last. Use if, elif, and else; do not stack separate if statements where one elif chain belongs.

POST 1. Visitors arrive carrying a pass of one of three colours. Implement gate_decision(pass_color) and return the right action:

    green  -> admit
    amber  -> hold
    red    -> deny

If the colour is anything else (a torn pass, a forged code, an empty string), the decision is not yours: return verify so the duty officer can look at it. Use an if-elif-else chain so the four outcomes are clearly mutually exclusive.
"""
def gate_decision(pass_color):
    if pass_color == "green":
        return "admit"
    elif pass_color == "amber":
        return "hold"
    elif pass_color == "red":
        return "deny"
    else:
        return "verify"