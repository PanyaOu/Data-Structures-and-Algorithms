def main():
    printSumTopDown(10, 0)
    print('-----------------------------')
    printSumDownUp(0, 10, 0)


def printSumTopDown(i, sum):
    if (i < 1):
        return
    print("sum of " + str(sum + i) + " is equal to " + str(sum) + "+ " + str(i))
    printSumTopDown(i - 1, sum + i)


def printSumDownUp(j, i, sum):
    if (j > i):
        return
    print("sum of " + str(sum + j) + " is equal to " + str(j) + "+ " + str(sum))

    printSumDownUp(j + 1, 10, sum + j)


if __name__ == '__main__':
    main()
