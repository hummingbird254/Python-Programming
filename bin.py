#maxNum = int(input("Enter max number:"))
numTerms = int(input("Enter number of terms:"))


def fib_upto_maxTerm(maxNum):
    seq = [0, 1]
    x = 0
    y = 1
    value = 0
    while value < maxNum:
        value = seq[x] + seq[y]
        seq.append(value)
        x = y
        y += 1
    return seq


def fib_for_numTerms(numTerms):
    seq = [0, 1]
    x = 0
    y = 1

    for v in range(2, numTerms):
        total = seq[x] + seq[y]
        seq.append(total)
        x = y
        y += 1
    return  seq


#print(fib_upto_maxTerm(maxNum))
print(fib_for_numTerms(numTerms))
