"""
Operation Watchpoint is over. The cohort reassembles in the briefing tent, still smelling of field rations and bad decisions. Sergeant Kay stands at the front, clipboard in one hand, red pen in the other. The After-Action Review covers every section of the exercise. Seven items on the board.

Some of these tasks use tools you have not been taught yet. That is intentional. Part of the review is researching what you need when the lesson has not handed it to you. The instructions will tell you exactly what to look up.

ITEM 3. Sergeant Kay says the sighting reports are too long. She wants them compressed. Run-length encoding replaces each consecutive run of the same character with the count followed by the character. AAABBC becomes 3A2B1C. A run of one still gets the prefix 1.

Implement run_length_encode(report), where report is a string. Walk the string with an index, counting each run. When the next character differs from the current one (or you reach the end), append the count and the character to the result, then reset the count.

For AAABBC the result is 3A2B1C. For an empty report the result is an empty string. (Kay also suggested compressing Idris's explanations, but there is no known algorithm for that.)
"""
def run_length_encode(report):
    if not report:
        return ""

    encoded = []
    current_char = report[0]
    count = 1

    for i in range(1, len(report)):
        if report[i] == current_char:
            count += 1
        else:
            encoded.append(f"{count}{current_char}")
            current_char = report[i]
            count = 1

    encoded.append(f"{count}{current_char}")

    return "".join(encoded)
