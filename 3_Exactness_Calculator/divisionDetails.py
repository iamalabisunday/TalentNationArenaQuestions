# Implement division_details(a, b). Return a dictionary with three keys: "true_division", "floor_division", and "remainder". true_division should be a / b rounded to 2 decimal places. floor_division should be a // b. remainder should be a % b.

def division_details(a, b):
    a_val = int(a)
    b_val = int(b)
    true_division = round(a_val / b_val, 2)
    floor_division = a_val // b_val
    remainder = a_val % b_val

    return {"remainder":remainder, "true_division": true_division, "floor_division": floor_division}