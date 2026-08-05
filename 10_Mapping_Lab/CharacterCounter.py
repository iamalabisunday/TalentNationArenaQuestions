# Implement character_counter(text). Return a dictionary where each character maps to how many times it appears. Count spaces and symbols too. Do not use collections.Counter.
def character_counter(text):
    lists = {}
    for char in text:
        lists[char] = lists.get(char, 0) + 1
    sorted_lists = dict(sorted(lists.items()))
    return sorted_lists