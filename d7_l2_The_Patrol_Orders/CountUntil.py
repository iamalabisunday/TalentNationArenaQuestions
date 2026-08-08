"""
Mid-morning the patrol gets stranger. The route is dotted with two kinds of marker that look similar at a glance and are not the same. A skip marker means walk past and keep going. A stop marker means the patrol ends here. Last week Recruit Idris's parallel patrol came back with a short count because he treated a stop as a skip. Sergeant Kay's warning to your section: read the orders before you write the loop. Today's tools are while, break, and continue.

JOB 1. Walk the route one character at a time. Count each one. The moment you hit the stop marker, the patrol ends; do not count the marker itself. Implement count_until(text, marker) using a for loop with break, or a while loop with an index.

For text ABCDE and marker C the count is 2 (A and B are counted, then C stops the patrol). If the marker never appears, count every character. An empty text counts zero.
"""
def count_until(text, marker):
    count = 0
    for char in text:
        if char == marker:
            break
        count += 1
    return count