# Implement receipt_formatter(name, quantity, price). Calculate subtotal as quantity multiplied by price. Calculate tax as 7.5 percent of subtotal. Calculate total as subtotal plus tax. Return a four-line report with labels Customer, Subtotal, Tax, and Total. Round subtotal, tax, and total to 2 decimal places.
def receipt_formatter(name, quantity, price):
    quantity = float(quantity)
    price = float(price)
    subtotal = quantity * price
    tax = (7.5/100) * subtotal
    total = subtotal + tax
    return (
        f"Customer: {name}\n"
        f"Subtotal: {subtotal}\n"
        f"Tax: {round(tax,2)}\n"
        f"Total: {round(total,2)}"
    )