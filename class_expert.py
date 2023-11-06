# everything is an object in python including classes, functions as demonstrated below

str1 = "joy"


class Goods:
    def __str__(self):
        return "Hi"


class Clothes(Goods):
    pass


ob = Clothes()
x = 4


def func():
    pass


# print(type(Clothes))
# print(str(ob))
# print(str(x))
# print(type(func))


def hello():
    class Hi:
        def prins(self):
            print("I'm here.")

    return Hi


x = hello()


# x.prins(self=None)


def add_attribute(self):
    self.z = 8


# creating classes from type constructor
Test = type("Test", (Goods, hello()), {"x": 5, "add_attribute": add_attribute})
v = Test()
v.c = 6
v.add_attribute()


# print(v.z)
# print(v.x)
# print(v.c)
# print(str(v))
# print()
# The code above is similar to the code below
# class Test:
#     def __init__(self):
#         self.x=5
#
# n=Test()
# n.c=7
# print(n.c)


# metaclasses
class Meta(type):
    def __new__(self, class_name, bases, attrs):
        print(attrs)
        a = {}
        for name, val in attrs.items():
            if name.startswith('__'):
                a[name] = val
            else:
                a[name.upper()] = val
        print(a)
        return type(class_name, bases, a)


class Employee(metaclass=Meta):
    x = 2
    y = 3

    def hello(self):
        print("hi")


emp1 = Employee()

print(emp1.X)
