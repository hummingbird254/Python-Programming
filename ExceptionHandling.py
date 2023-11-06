try:
    x=int(3)
except ValueError:
    print("Enter correct values!")
except NameError:
    print("What is that?")
else:
    print("Value is",x)