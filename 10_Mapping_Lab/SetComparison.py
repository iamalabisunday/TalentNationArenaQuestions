# Implement set_comparison(a, b). Return a dictionary with keys named both, only_a, and only_b. The both value should be a sorted list of items in both lists. The only_a value should be a sorted list of items only in a. The only_b value should be a sorted list of items only in b.
def set_comparison(a, b):
    set_a = set(a)
    set_b = set(b)
    
    # Perform set operations and convert results to sorted lists
    both = sorted(set_a & set_b)
    only_a = sorted(set_a - set_b)
    only_b = sorted(set_b - set_a)
    
    return {
        "both": both,
        "only_a": only_a,
        "only_b": only_b
    }