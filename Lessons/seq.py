# List - non-unique sequence
a_list = [
    10, 10, 11, 5, 12, 6,
]
# or
# a_list = list(10, 10, 11,)

# Tuple - non-changable sequence
a_tuple = (10,)
# or
# a_tuple = tuple(10)

# Set - unique sequence
a_set = {10, 11,}
# or
# a_set = set(10, 11,)

a_empty_set = set()

# String - a sequence of chars
a_str = "hello"


# Element by index
print(a_list[1])  # second element

# Sub-sequence
print(a_list[1:3])  # elements from second to third

# Checks if element in the sequence
5 in a_list == True
