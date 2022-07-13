# Simple function / procedure
def hello():
    print("Hello, world!")

hello()

# functions are objects too
def get_my_name():
    return "Serhii"

get_my_name.description = "Returns my name!"

print(get_my_name())
print(get_my_name.description)

# With return value
def get_year():
    return 2022

current_year = get_year()

# With arguments
def get_total(price, count):
    return price * count

total = get_total(10, 2)

# With optional arguments
def greeting(name, last_name=None):
    full_name = name if last_name is None else "{} {}.".format(name, last_name[0])

    print(f"Welcome, {full_name}!")

greeting("Serhii")
greeting("Anna", last_name="Lee")

# With variable agrumens
def calculate(op, *args):
    """Calculates using 'op' on list of arguments

    :param op: the operation
    """
    if not args:
        print("Not enought arguments")
        return

    if op == "+":
        return sum(args)

print(calculate("+"))
print(calculate("+", 1, 2, 10, 5))

# With variable positional and keyword arguments
def register(name, age=None, *args, **kwargs):
    print(name, age, args, kwargs)

register("Serhii")
register("Serhii", 1, 2)
register("Serhii", age=18)
register("Serhii", 100, 1200, last_name="Diachok")

# With doc string
def welcome():
    "This is a simple welcoming function."

    print("Welcome to the Python world!")

welcome()
# help(welcome)
print(welcome.__doc__)
