"""
Dawn patrol on Day Two of Operation Watchpoint. Your section steps off into the perimeter sweep at oh-six-hundred. Three jobs across the morning, each one a small for loop. Today is the day the loop stops being a spelling and starts being a tool.

JOB 2. The patrol log is a single string of marks: X for a sighting, O for clear, dot for an empty checkpoint. Implement count_sightings(report) and return how many sightings the patrol made. Iterate over the report one character at a time with a for loop. Do not use the string method .count(); the point of the lesson is to walk the loop yourself.

For the report XOXOX the count is 3. An empty report has zero sightings.
"""
def count_sightings(report):
    count = 0
    for c in report:
        if c == "X":
            count += 1
    return count