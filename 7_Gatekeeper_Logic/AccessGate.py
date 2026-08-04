# Implement access_gate(age, has_id, is_banned). Use guard-clause style. Return Too young if age is less than 18. Return No ID if has_id is false. Return Banned if is_banned is true. Return Allowed only if all checks pass.
def access_gate(age, has_id, is_banned):
    if age < 18:
        return "Too young"
    elif has_id is False:
        return "No ID"
    elif is_banned is True:
        return "Banned"
    return "Allowed"