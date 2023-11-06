class Animal:
    def __init__(self, name):
        self.name = name

    def breathe(self):
        print("{0} breathes air.".format(self.name))

    def drink(self):
        print("{0} drinks water.".format(self.name))


class Lion(Animal):
    """
    def __init__(self):
        print("This is a Lion.")
    """

    def talk(self):
        print("{0} roars.".format(self.name))

class Cat(Animal):
    def __init__(self, x):
        super().__init__(x)

    def talk(self):
        print("Cat purrs.")



class Goat(Animal):
    def talk(self):
        print("{0} bleats.".format(self.name))


l1 = Lion("Mufasa")
l1.breathe()
l1.talk()

g1 = Goat("Billy")
g1.drink()
g1.breathe()
g1.talk()

c1=Cat("Nuggets")
c1.drink()
c1.talk()