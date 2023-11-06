import sys
import timeit

xlist = ["Ball", "Mango", "Tennis", "Class"]
ylist = xlist.copy()  # ylist=xlist[:] or ylist=list(xlist)
xlist.append("Grave")
xlist.insert(1, "Dave")
xlist.pop(0)
# xlist.clear()
xlist[0] = "Mum"
count = len(xlist)
xlist.reverse()
print(xlist)
for x in range(count):
    print(xlist[x])

for v in xlist:
    print(v)
# slicing technique(check in video on more about this technique)

print(xlist[::-1])
print(ylist[::2])
print(ylist[2:])

numbers0 = [1, 2, 2, 3, 4, 5, 6]
zlist = [x * x for x in numbers0]
print(zlist)
print(numbers0.count(2))

print(sys.getsizeof(numbers0), "bytes")
print(timeit.timeit(stmt="[1, 2, 2, 3, 4, 5, 6]", number=1000000))

# note that tuples are more efficient to work with. Takes less memory and less time. Tuples are immutable
# dictionaries have keys
# sets are unordered, immutable and do not allow duplicates
