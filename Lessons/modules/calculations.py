def get_total(number, price):
    print("Calculating total...")
    return number * price

def get_total_with_discount(number, price, discount=0.1):
    print("Calculating total with discount...")

    total = get_total(number, price)
    return total - total*discount

# print("This is calculations.py module")
# input("Type something: ")
