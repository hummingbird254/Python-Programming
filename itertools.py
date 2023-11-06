from itertools import count, cycle, repeat, groupby

a = [10, 11, 12, 13]

for x in repeat(a, 3):
    print(x)
''''
for x in cycle(a): # will print infinitely unless stop argument given
    print(x)
'''
for v in count(5):
    print(v)
    if v == 15:
        break
