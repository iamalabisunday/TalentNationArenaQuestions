"""
Mid-morning the patrol gets stranger. The route is dotted with two kinds of marker that look similar at a glance and are not the same. A skip marker means walk past and keep going. A stop marker means the patrol ends here. Last week Recruit Idris's parallel patrol came back with a short count because he treated a stop as a skip. Sergeant Kay's warning to your section: read the orders before you write the loop. Today's tools are while, break, and continue.

JOB 2. The patrol log uses a dot for an inactive checkpoint. Inactive checkpoints are not counted but they do not end the patrol either: just walk past them and keep going. Implement count_active(report). Iterate over the report; for each dot, use continue to skip to the next character; every other character counts.

For the report A.B.C the count is 3. A report of all dots counts zero. This is the case Idris got wrong last week: he treated a dot the way Job 1 treats the marker.
"""
def count_active(report):
    count = 0
    for n in report.lower():
        if "a" <= n <= "z":
            count += 1
    return count