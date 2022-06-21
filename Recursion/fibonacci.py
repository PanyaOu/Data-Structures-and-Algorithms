def main():
    print(fib(6))


def fib(i):
    if i < 2:
        return i
    return fib(i-1) + fib(i-2)


if __name__ == '__main__':
    main()
