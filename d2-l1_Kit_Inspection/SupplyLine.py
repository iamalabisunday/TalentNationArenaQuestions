# The quartermaster logs one line per item. The item is a string, the quantity is a whole number, and the unit weight is a decimal number of kilograms. Implement supply_line(item, quantity, unit_weight) and return one line in this exact shape: the quantity, a space, the letter x, a space, the item, a space, the at sign, a space, the unit weight, kg, a space, the equals sign, a space, then the total weight followed by kg. For 3 rifles at 0.5kg each the line is 3 x rifle @ 0.5kg = 1.5kg. Notice that multiplying a whole number by a decimal gives a decimal.
def supply_line(item, quantity, unit_weight):
    item = str(item)
    quantity = int(quantity)
    unit_weight = float(unit_weight)
    total_weight = quantity * unit_weight
    return f"{quantity} x {item} @ {unit_weight}kg = {total_weight}kg"