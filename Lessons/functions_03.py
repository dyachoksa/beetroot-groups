# def add_10(value):
#     return value + 10

# def add_20(value):
#     return value + 20

# def add_30(value):
#     return value + 30

def make_add(n):
    def add(value):
        return value + n
    return add

add_10 = make_add(10)
add_20 = make_add(20)
add_30 = make_add(30)

if __name__ == "__main__":
    value = 5
    print("Value:", value)
    print("Adding 10:", add_10(value))
    print("Adding 20:", add_20(value))
    print("Adding 30:", add_30(value))

    value = int(input("Enter a value: "))
    adder = int(input("Enter a number to add: "))

    func = make_add(adder)
    print("Adding", adder, "to", value, ":", func(value))
