from functools import reduce

w = [8, 3, 12, 6, 9, 2]

b = reduce(lambda x, y: x * y, w)
print(b)

s = map(lambda x: x * 2, w)
print(list(s))

s_easy = [x * 2 for x in w]  # list comprehension technique
print(s_easy)

e = filter(lambda x: x % 2 == 0, w)
print(list(e))

e_easy = [x for x in w if x % 2 == 0]
print(e_easy)

add5 = lambda x: x + 5
print(add5(4))

multVar = lambda x, y: x * y
print(multVar(4, 3))

cartesianPoints = [(2, 1), (-6, 7), (3, 2), (8, 0), (0, 2)]

sortedPoints = sorted(cartesianPoints)  # sort by x
print(sortedPoints)

sortedPoints1 = sorted(cartesianPoints, key=lambda x: x[1])  # sort by y
print(sortedPoints1)

sortedPoints2 = sorted(cartesianPoints, key=lambda x: x[0] + x[1]) # sort by sum of x and y
print(sortedPoints2)
