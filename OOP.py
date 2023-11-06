class Student:
    sCount = 0

    def __init__(self, name, age):
        if not isinstance(name, str):
            raise TypeError("Must be a string.")
        self.name = name
        if not isinstance(age, int):
            raise TypeError("Must be an integer.")
        self.age = age
        Student.sCount += 1

    def displayDetails(self):
        print(self.name, self.age)


class ComplexNum:
    def __init__(self, real, imag):
        if not isinstance(real, int):
            raise TypeError
        self.real = real
        if not isinstance(imag, int):
            raise TypeError
        self.imag = imag

    def getNum(self):
        print("{0} + {1}j".format(self.real, self.imag))


name1 = str(input("Enter your name:\n"))
age1 = int(input("Enter your age:\n"))
p1 = Student(name1, age1)

name2 = str(input("Enter your name:\n"))
age2 = int(input("Enter your age:\n"))
p2 = Student(name2, age2)
# print(p1.age)
print(Student.sCount)

c1 = ComplexNum(int(23),int(54))
c1.getNum()

print(Student.__name__)
print(Student.__doc__)
