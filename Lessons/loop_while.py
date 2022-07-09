# while True:
#     # do something
#     pass


i = 1
while i <= 10:
    print("*" * i)
    i += 1
    # or
    # i = i + 1

x = 0
while x < 10:
    if x == 5:
        # raise ValueError()
        break

    print(x)
    x += 1
else:
    print("The loop was ended")
