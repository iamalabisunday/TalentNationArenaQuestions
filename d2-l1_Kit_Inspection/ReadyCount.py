# Kit inspection. Each of the three arguments is a boolean: True if that piece of kit passed inspection, False if it did not. Implement count_ready(weapon, ammo, comms) and return how many of the three passed, as a whole number. A boolean is a kind of number in Python, so you do not need any decisions to count them. For weapon True, ammo False, comms True the answer is 2.
def count_ready(weapon, ammo, comms):
    count = 0
    if str(weapon).lower() == "true":
        count += 1
    if str(ammo).lower() == "true":
        count += 1
    if str(comms).lower() == "true":
        count += 1
    return count