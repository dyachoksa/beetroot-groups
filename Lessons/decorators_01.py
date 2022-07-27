def do_several_times(f=None, n=2):
    print("Excuting", do_several_times.__name__)

    def wrapper(func):
        print("Excuting", wrapper.__name__)

        def inner():
            print("Excuting", inner.__name__)
            for _ in range(n):
                func()

        return inner    

    if f is None:
        return wrapper

    print("Executing wrapper(f)")
    return wrapper(f)


@do_several_times(n=3)
def print_hello():
    print("Excuting print_hello")
    print("Hello, world!")

# print_hello = do_several_times(print_hello)


if __name__ == "__main__":
    print("Executing main")
    print_hello()
