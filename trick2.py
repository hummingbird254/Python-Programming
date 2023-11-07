class Expenses:
    def __init__(self, name, cost):
        if type(name) != str:
            raise Exception("Kindly input a string for the name!")
        else:
            self.name = name
        if type(cost) != int:
            raise Exception("Kindly input an integer for the cost!")
        else:
            self.cost = cost

    def __str__(self):
        return self.name

    def __add__(self, other):
        return self.cost + other.cost


first = Expenses("Food ", 40000)
second = Expenses("Transport", 20000)

print(first+second)
