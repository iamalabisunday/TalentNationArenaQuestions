#Implement score_summary(name, a, b, c). Convert the three score values to numbers. 
# If conversion fails, return Invalid score. If any score is below 0 or above 100, 
# return Invalid score. Otherwise calculate the average, round it to 2 decimal places, 
# choose a grade, and return a three-line report with labels Student, Average, and Grade. 
# Grade is A for 90 and above, B for 80 and above, C for 70 and above, and F below 70.


def score_summary(name, a, b, c):
    try:
        a = float(a)
        b = float(b)
        c = float(c)
    except ValueError:
        return "Invalid score"

    if a < 0 or b < 0 or c < 0 or a > 100 or b > 100 or c > 100:
        return "Invalid score"

    average = (a + b + c) / 3
    average_dec = round(average, 2)

    if average >= 90:
        result = "A"
    elif average >= 80:
        result = "B"
    elif average >= 70:
        result = "C"
    else:
        result = "F"
        
    return f"Student: {name}\nAverage: {average_dec}\nGrade: {result}"