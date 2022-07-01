def main():
    arr = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    n = len(arr) + 1
    print(minCostClimbStairsTDMemo(n, arr))


def minCostClimbStairsTDMemo(n, arr):
    if n < 3:
        return min(arr[0], arr[1])
    dp = [0] * n
    dp[n - 2] = arr[n - 2]
    dp[n - 3] = arr[n - 3]
    for x in range(n - 4, -1, -1):
        step = arr[x] + min(dp[x + 1], dp[x + 2])
        dp[x] = step
    return min(dp[0], dp[1])


if __name__ == '__main__':
    main()
