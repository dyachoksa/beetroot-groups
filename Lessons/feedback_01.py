# Sample

while True:
    p = int(input("Enter a number (form 1 to 10): "))

    if p == 6:
        print("Amazing!")
        break

    print("Try again!")

# Not good
for i in range(10):
    if i % 2 == 0:
        print(i)
    else:
        if i % 5 == 0:
            continue
        else:
            print("Next iteration")

# Better
for i in range(10):
    if i % 5 == 0:
        continue

    if i % 2 == 0:
        print(i)
        continue

    print("Next iteration")

s = 5 > 4
name = "Sergii"

# Not good
if s != True:
    print("Something")

if name.isdigit() == True:
    pass

if s == None:
    pass

# Better
if not s:
    print("Something")

if name.isdigit():
    pass

if s is None:
    pass

list01 = []
# Instead of
if len(list01) > 0:
    print("Do something...")

# can be
if list01:
    print("Do something...")
