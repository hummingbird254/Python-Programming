fib_list = [1, 1]
x = 0
y = 1

for v in range(10):
    total = fib_list[x] + fib_list[y]
    fib_list.append(total)
    x = y
    y += 1

print(fib_list)
