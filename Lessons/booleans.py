# Boolean values:
a_true = True
a_false = False

# AND
# True and True => True
# True and False => False
# False and True => False
# False and False => False

# OR
# True or True => True
# True or False => True
# False or True => True
# False or False => False

# NOT
# not True => False
# not False => True

a = 12
b = 11
c = 0
d = 5

if a > b:
    sum = 2 + 2
    print("This is a True!")
    print("2 + 2 =", sum)
else:
    print("Not good at all...")

# a and b or c and d
# True and True or False and True
if a and b or c and d:
    print(True)
else:
    print(False)

age = 60
print("Your age:", age)
if age < 21 or age > 30:
    print("You are not allowed here!")
else:
    print("You are welcome!")

# with AND
if (age >= 21 and age <= 30) or age == 60:
    print("You are welcome!")
else:
    print("You are not allowed here!")

# with vars
age_between_21_and_30 = age >= 21 and age <= 30
age_is_60 = age == 60

if age_between_21_and_30 or age_is_60:
    print("You are welcome!")
else:
    print("You are not allowed here!")

# with not
if not (age_between_21_and_30 or age_is_60):
    print("You are not allowed here!")
else:
    print("You are welcome!")

# chains
if 21 <= (age <= 30):
    print("You are welcome!")

# if False:
#     pass
# elif False:
#     pass
# else:
#     pass
