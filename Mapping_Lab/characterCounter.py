# Implement character_counter(text). Return a dictionary where each character maps to how many times it appears. Count spaces and symbols too. Do not use collections.Counter.
def character_counter(text):
    counts = {}
    for char in text:
        counts[char] = counts.get(char, 0) + 1
    return counts