# No bad, but not good
# def make_operation(operation, *args):
#     if args:
#         operands = list(args)
#         x = operands.pop(0)
#         if operation == "+":
#             while operands:
#                 x += operands.pop(0)
#             return x
#         if operation == "-":
#             while operands:
#                 x -= operands.pop(0)
#             return x
#         if operation == "*":
#             while operands:
#                 x *= operands.pop(0)
#             return x
#     print("Wrong operation or empty operands!")
#     exit(-1)

# Better
def make_operation(operation, *args):
    if not args:
        print("Empty operands!")
        exit(-1)
    
    if operation not in ["+", "-", "*", "/"]:
        print("Wrong operation!")
        exit(-1)

    for arg in args:
        if type(arg) != int:
            raise ValueError("Operand not int")
        
        if operation == "/" and arg == 0:
            raise ValueError("Can't divide by 0")
    
    operands = list(args)
    x = operands.pop(0)

    while operands:
        if operation == "+":
            x += operands.pop(0)
        elif operation == "-":
            x -= operands.pop(0)
        elif operation == "*":
            x *= operands.pop(0)
        elif operation == "/":
            x /= operands.pop(0)

        # or
        # x = {
        #     "+": lambda n: x + n,
        #     "-": lambda n: x - n,
        #     "*": lambda n: x * n,
        #     "/": lambda n: x / n,
        # }[operation](operands.pop(0))
    
    return x


print(make_operation('+', 7, 7, 2))
print(make_operation('-', 5, 5, -10, -20))
print(make_operation('*', 7, 6))
print(make_operation('*'))
