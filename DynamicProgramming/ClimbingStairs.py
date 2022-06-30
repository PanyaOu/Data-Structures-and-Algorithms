def main():
    print(climbStairs(5))


def climbStairs(n):
    dp = [0, 1, 2, 3]
    if n < 4:
        return dp[n]
    for x in range(3, n+1):
        dp.append(dp[x] + dp[x-1])
    return dp[n]


if __name__ == '__main__':
    main()
