def main():
    print(factorial(5))


def factorial(i):
    if i <= 0:
        return 1
    return i*factorial(i-1)


if __name__ == '__main__':
    main()
