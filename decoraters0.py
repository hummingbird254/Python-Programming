# use cases include: validating input, timers, logging, checking return values

import time


def func(f):
    def wrapper(*args, **kwargs):
        print("Started")
        f(*args, **kwargs)
        print("Ended")

    return wrapper


def func1(v):
    print(f"{v}...working")


# func(func1)()

# decoraters

@func
def func1(v):
    print(f"{v}...working")


# func1(5)


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        rv = func()
        total = time.time() - start
        print("Time:",total)
        return rv
    return wrapper

@timer
def test():
    for _ in range(100000):
        pass


@timer
def test1():
    time.sleep(3)


test1()