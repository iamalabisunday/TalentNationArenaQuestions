"""
Mid-morning the patrol gets stranger. The route is dotted with two kinds of marker that look similar at a glance and are not the same. A skip marker means walk past and keep going. A stop marker means the patrol ends here. Last week Recruit Idris's parallel patrol came back with a short count because he treated a stop as a skip. Sergeant Kay's warning to your section: read the orders before you write the loop. Today's tools are while, break, and continue.

JOB 3. The scout has been told to find the first occurrence of a callsign character in the route log and report back its position. Implement find_first(text, target) using a while loop with an index. Return the position the first time text at that index equals target. If the target never appears, return -1.

For text ABCABC and target C the answer is 2. For an empty text or a target that does not appear, the answer is -1. Do not use .find() or .index() (those exist, but the lesson is to write the search yourself with a while loop and an index).
"""
def find_first(text, target):
    index = 0
    while index < len(text):
        if text[index] == target:
            return index
        index += 1
    return -1