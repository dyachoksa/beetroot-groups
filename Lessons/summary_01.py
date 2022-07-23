import random

# Data types
a_int = 10
a_float = 1.25
a_complex = 1 + 1j
a_bool = True
a_str = "Hello"
a_none = None
a_list = [1, "h", False, None, 125]
a_tuple = (1, 1)
a_set = {10, 12}
a_dict = {"key": "value", True: "True", False: False, None: "This is none!"}

## control structures
# if sentenses
if a_bool and a_int > 5:
    print("This is True!")
else:
    print("This is False!")

# is vs ==
"Hello" == "Hello"
a_none is None # True
a_none == None # True

# not recommended
if a_bool == True: pass
# better
if a_bool: pass

# loops
i = 0
while i < 10:
    print("*" * i)
    i += 1

for item in a_list:
    print(item)

for i in range(10):
    for j in range(5):
        print(i, j, i+j)

# exceptions
try:
    print(a_list[10])
except IndexError:
    print("Index not found")
finally:
    print("Try ended.")

# functions
def calculate_total(qty, price, tax=None, discount=None):
    if qty < 0:
        raise ValueError("Quantity shouyld be positive")

    total = qty * price

    if tax is not None:
        total += total*tax

    if discount is not None:
        total -= total*discount

    return total

total = calculate_total(10, 10, tax=0.05, discount=0.1)
print("Total =", total)

# useful operators and constructions
list_random_10 = [random.randint(1, 100) for _ in range(10)]
dict_random_10 = {f"num_{i}": random.randint(1, 100) for i in range(10)}

# context manager
with open("data.txt") as f:
    data = f.read()

    # read and return one line
    # data = f.readline()

    # read and return all lines from file as list
    # data = f.readlines()

print("File content:")
print(data)
