def main():
    nums = [200, 3, 140, 20, 10]
    n = len(nums)
    print(houseRobber2(nums, n))


def houseRobber2(arr, n):
    if n == 1:
        return arr[0]
    if n == 2:
        return max(arr)
    dp = [0] * n
    dp2 = [0] * n
    dp[0] = arr[0]
    dp[1] = max(arr[0], arr[1])
    dp[2] = max(dp[1], arr[2] + arr[0])

    dp2[1] = arr[1]
    dp2[2] = max(arr[1], arr[2])

    for x in range(3, n):
        dp2[x] = max(arr[x] + dp2[x - 2], dp2[x - 1])
        if x == n - 1:
            break
        else:
            dp[x] = max(arr[x] + dp[x - 2], dp[x - 1])
    print(dp, dp2)
    return max(dp[n - 2], dp2[n - 1])


if __name__ == '__main__':
    main()
