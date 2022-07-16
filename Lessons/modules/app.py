# import sys

# print(sys.path)

# import full module
import calculations

# or just something from it
from calculations import get_total_with_discount

number = int(input("Number of items: "))
price = float(input("Price of the item: "))

total = calculations.get_total(number, price)
print("Total amount:", total)

total_with_discount = get_total_with_discount(number, price, 0.25)
print("Total amount with discopunt (25%):", total_with_discount)
