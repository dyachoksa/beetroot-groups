# Non-changable types
# bool (True, False), None, int, float, str, tuple, 'function', 'class'
a_empty_dict = {}

# a_empty_dict = dict()

a_bool_dict = {
    True: "This is True",
    False: "This is False"
}

a_tuple_dict = {
    (1, 0): "(1, 0)",
    (0, 0): "(0, 0)",
    (1, 1): "(1, 1)",
    (1, 1, 2): "(1, 1, 2)",
}

a_dict = {
    "name": "Sergey",
    "age": 18,
}

print(a_bool_dict[True])
print(a_tuple_dict[(1, 0)])
print(a_dict["name"])
