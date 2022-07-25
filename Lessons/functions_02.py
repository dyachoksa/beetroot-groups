def print_welcome():
    print("Welcome to my program!")
    print("I hope you enjoy it.")
    print("Have a nice day!")


def add_star(value):
    return value + "*"

def add_question(value):
    return value + "?"

def add_exclamation(value):
    return value + "!"

def add_hash(value):
    return value + "#"

function_as_value = {
    "*": add_star,
    "?": add_question,
    "!": add_exclamation,
    "#": add_hash,
}

function_as_key = {
    add_star: "*",
    add_question: "?",
    add_exclamation: "!",
    add_hash: "#",
}

def apply(value, functions):
    for function in functions:
        print("Applying function:", function_as_key[function])
        value = function(value)

    return value

def interactive_apply():
    value = input("Enter a value: ")
    functions = []

    print("Available functions:")
    for label, name in function_as_value.items():
        print(label, name.__name__)

    while True:
        function = input("Enter a function (or 'done'): ")
        if function == "done":
            break
        functions.append(function_as_value[function])

    print("Result:", apply(value, functions))


if __name__ == "__main__":
    print_welcome()

    print(apply("Hello", [add_star, add_question, add_exclamation]))
    print(apply("Hello", [add_question, add_hash, add_exclamation, add_star]))
    print(apply("World", [add_star, add_exclamation, add_hash]))

    interactive_apply()
