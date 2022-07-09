import random

# Plain list creation and filling
random_numbers = []
for _ in range(10):
    random_numbers.append(random.randint(1, 100))

print(random_numbers)

# List comprehensions
numbers = [x**x for x in [2, 4, 3, 1]]
random_numbers = [random.randint(1, 100) for _ in range(10)]
random_numbers_even = [n for n in range(10, 100, 3) if n % 2 == 0]

print(random_numbers)
print(random_numbers_even)


data = [("name", "Sergey"), ("age", 18)]

# Plain dict creation
user = {}
for col_name, col_value in data:
    user[col_name] = col_value

print(user)

# Dict comprehensions
user = {col_name: col_value for col_name, col_value in data}
# or
# user = {col[0]: col[1] for col in data}

print(user)
