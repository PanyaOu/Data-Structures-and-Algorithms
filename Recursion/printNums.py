def main():
    printSeq(5)


def printSeq(i):
    if (i < 1):
        return
    print(i)
    printSeq(i-1)


if __name__ == '__main__':
    main()
