class Fraction():

    def __init__(self, num, den):
        self.num = num
        self.den = den

    def display_as_fraction(self):
        return f"{self.num}/{self.den}"

    def display_as_decimal(self):
        try:
            total = float(self.num / self.den)
        except ZeroDivisionError:
            print("You're dividing by zero. Make the denominator to be 1 if you want a whole number.")
        return f"{total:.2f}"

    def format(self):
        try:
            actual = float(self.num / self.den)
        except ZeroDivisionError:
            print("You're dividing by zero. Make the denominator to be 1 if you want a whole number.")
        return actual

    def add(self, y):
        try:
            x = float(self.num / self.den)
        except ZeroDivisionError:
            print("You're dividing by zero. Make the denominator to be 1 if you want a whole number.")
        y_dec = y.format()
        return f"{round(x + y_dec, 2)}"

        return f"{total}"

    def subtract(self, y):
        try:
            x = float(self.num / self.den)
        except ZeroDivisionError:
            print("You're dividing by zero. Make the denominator to be 1 if you want a whole number.")
        y_dec = y.format()
        if x >= y_dec:
            return f"{round(x - y_dec, 2)}"
        elif x < y_dec:
            return f"{round(y_dec - x, 2)}"


c = Fraction(3, 4)
d = Fraction(1, 2)

print(c.add(d))
