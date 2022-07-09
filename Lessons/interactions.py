name = input("Enter your name: ")

age = input("Enter your age: ")
if not age.isdigit():
    print("Age should be an integer!")
else:
    next_age = int(age) + 1
    print(name, next_age)
