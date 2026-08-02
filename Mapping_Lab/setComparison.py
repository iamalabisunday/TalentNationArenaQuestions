# Implement set_comparison(a, b). Return a dictionary with keys named both, only_a, and only_b. The both value should be a sorted list of items in both lists. The only_a value should be a sorted list of items only in a. The only_b value should be a sorted list of items only in b.

def set_comparison(a, b):
    # Convert input lists into sets for O(1) mathematical set operations
    set_a = set(a)
    set_b = set(b)
    
    return {
        "both": sorted(list(set_a & set_b)),   # Intersection: elements in both sets
        "only_a": sorted(list(set_a - set_b)), # Difference: elements in a but not b
        "only_b": sorted(list(set_b - set_a))  # Difference: elements in b but not a
    }