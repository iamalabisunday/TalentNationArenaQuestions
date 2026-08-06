"""
Some stores items are measured in decimals, so the check must allow a single decimal point. Implement safe_measure(raw), where raw is a string from a form. Trim the text. If removing one decimal point leaves a run of digits, the form is a valid measurement, so return it converted to a decimal number. Otherwise return the string invalid. This is the same idea as the quantity check, widened to accept one point. The form 3.14 returns the number 3.14; the form 3.14.15 has two points and returns invalid.
"""
def safe_measure(raw):
    num = raw.strip()
    
    if num.replace(".", "", 1).isdigit():
        return float(num)
        
    return "invalid"