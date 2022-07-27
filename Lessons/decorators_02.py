import functools
import time


def debug(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signature})")
        print(f"Annotations {func.__annotations__!r}")

        for k, v in kwargs.items():
            if k not in func.__annotations__:
                continue

            if type(v) is not func.__annotations__[k]:
                raise ValueError(f"{k} in not of type {func.__annotations__[k].__name__}")

        value = func(*args, **kwargs)

        print(f"{func.__name__!r} returned {value!r}")
        return value

    return inner


def timer(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        start_time = time.perf_counter()
        
        value = func(*args, **kwargs)

        end_time = time.perf_counter()
        run_time = end_time - start_time

        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")

        return value

    return inner


@timer
@debug
def print_welcome():
    print("Hello, World!")
    # emulate long-running task
    time.sleep(1)


@timer
@debug
def get_total(amount: float, tax: float, discount: float = None):
    return amount + (amount * tax)


@timer
def waste_time(n):
    for _ in range(n):
        sum([i**2 for i in range(10000)])


if __name__ == "__main__":
    print_welcome()

    print(get_total(1000, 0.05, discount=0.1))

    waste_time(1)
    waste_time(10)
    waste_time(99)
    waste_time(150)
