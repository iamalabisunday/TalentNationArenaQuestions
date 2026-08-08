"""
Every callsign begins with a three-letter unit prefix. Implement prefix_code(callsign) and return the first three characters. Use a slice, not three separate index reads. If the callsign is shorter than three characters, a slice simply returns whatever is there without raising an error, which is the behaviour you want.
"""
def prefix_code(callsign):
    return callsign[0:3]