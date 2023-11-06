import sys


# this code induces a memory overload
# x = [i ** 2 for i in range(1000000000)]
# for y in x:
#     print(y)

# a much better way to achieve the above with storing in a list
# for v in range(1000000000):
#     print(v ** 2)


# generator
def gen(n):
    for i in range(n):
        yield i ** 2


x = [v ** 2 for v in range(1000)]
d = gen(1000)

print(next(d))
print(next(d))
print(next(d))

print(sys.getsizeof(x))
print(sys.getsizeof(d))
