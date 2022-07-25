import operator
import pprint

users = [
    {"email": "user@example.com", "name": "John Smith", "age": 30},
    {"email": "user@test.com", "name": "Jane Doe", "age": 25},
    {"email": "me@example.com", "name": "Me Myself", "age": 27},
]

def sort_users(users):
    return sorted(users, key=lambda user: user["name"])

def sort_users_by_age(users):
    def get_age(user):
        return user["age"]

    print("Function to get value:", get_age.__name__)

    return sorted(users, key=get_age)

def sort_users_by_email(users):
    return sorted(users, key=operator.itemgetter("email"))

sorted_users_by_name = sort_users(users)
sorted_users_by_age = sort_users_by_age(users)

print("Sorted by name:")
pprint.pprint(sorted_users_by_name, sort_dicts=False)

print("Sorted by age:")
pprint.pprint(sorted_users_by_age)

print("Sorted by email:")
pprint.pprint(sort_users_by_email(users))
