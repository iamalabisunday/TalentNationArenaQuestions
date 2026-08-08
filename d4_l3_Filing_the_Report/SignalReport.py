"""
File a one-line signal report. Implement signal_report(callsign, strength). The callsign is right-aligned in a field eight characters wide, then a space, a vertical bar, a space, then the strength shown as a percentage to one decimal place. The strength arrives as a fraction, so 0.073 reports as 7.3%. For callsign HAWK and strength 0.073 the report is four spaces, HAWK, space, bar, space, 7.3%. A callsign longer than eight characters is not cut; the field simply grows.
"""
def signal_report(callsign, strength):
    return f"{callsign:>8} | {strength:.1%}"
