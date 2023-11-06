array = [4, 3, 3, 2, 2, 2, 1]


def monotone(array):
    x = 0
    y = 0
    error = 0
    for v in range(len(array) - 1):
        if array[v] <= array[v + 1]:
            x += 1
        elif array[v] >= array[v + 1]:
            y += 1
        else:
            error += 1
    if x == len(array) - 1:
        return True
    elif y == len(array) - 1:
        return True
    else:
        return False


print(monotone(array))
