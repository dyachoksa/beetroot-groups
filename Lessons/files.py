# plain usage
try:
    print("Opennig file...")
    f = open("data.txt", "a+")

    # reading
    data = f.read()

    # writing
    f.write("Hello, World!\n")
except IOError as err:
    print("File error:", str(err))
except:
    print("Something went wrong")
finally:
    print("Closing file...")
    f.close()

# usage with context managers
with open("data.txt", "a+") as f:
    # reading
    data = f.read()

    # writing
    f.write("Hello, World!\n")

# read line by line
# not good
with open("data.txt") as f:
    line = f.readline()
    while line:
        print(line)
        line = f.readline()

# better
with open("data.txt") as f:
    for line in f:
        print(line)
