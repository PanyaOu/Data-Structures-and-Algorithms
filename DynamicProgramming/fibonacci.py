def main():
    print(fib(100))


def fib(n):
    dp = [0, 1]
    if n < 2:
        return dp[n]
    for x in range(2, n+1):
        dp.append(dp[x-1] + dp[x-2])
    return dp[n]


if __name__ == '__main__':
    main()
