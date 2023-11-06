myTuple = ("Mic", 34, "Male")
myTuple0 = "Shely", 21, "Female"
myTuple1 = ("Tom",)
myTuple2 = tuple(["Mary", 30, "Female"])

myList = list(myTuple)
print(myList)
name, age, gender = myTuple0
print(name)

myTuple3 = ('b', 'l', 'a', 'a', 'c')

print(myTuple3.count('a'))
print(myTuple3.index('l'))
print(myTuple3[1:3])
print(myTuple3[::-1])
# basically tuples are immutable lists
