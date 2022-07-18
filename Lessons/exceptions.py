try:
    # ZeroDivisionError
    # print(1/0)

    # IndexError
    a_list = [1, 0]
    # print(a_list[2])

    # Custom error
    raise ValueError("Bad value...")
# Particular exception type
except ZeroDivisionError:
    print("You can't divide by 0!")
except IndexError:
    print("Unknown index!")
# All possible exceptions
except:
    print("Something went wrong!")
finally:
    print("try/except completed")

print(a_list)

print("This is the end of exceptions.py")
