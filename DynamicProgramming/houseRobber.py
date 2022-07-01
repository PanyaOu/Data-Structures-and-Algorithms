def main():
    #nums = [2, 1, 1, 2]
    #nums = [1, 2, 3, 1]
    nums = [1, 7, 9, 4, 7, 8]
    n = len(nums)
    print(houseRobber(nums, n))


def houseRobber(arr, n):
    dp = [0] * n
    if n <= 2:
        return max(arr)

    dp[0] = arr[0]
    dp[1] = max(arr[0], arr[1])
    for x in range(2, n):
        dp[x] = max(arr[x] + dp[x - 2], dp[x - 1])

    return dp[n-1]


if __name__ == '__main__':
    main()
