def main():
    arr = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    # start at either index 1 or 0 then follow the equation
    # print(min(minCostClimbStairsBU(0, arr), minCostClimbStairsBU(1, arr)))
    # start at either index n-1 or n-2 then follow the equation
    print(min(minCostClimbStairsTP(len(arr) - 1, arr), minCostClimbStairsTP(len(arr) - 2, arr)))


# bottom up
def minCostClimbStairsBU(idx, arr):
    if idx > len(arr) - 1:
        return 0
    stepOne = minCostClimbStairsBU(idx + 1, arr)
    stepTwo = minCostClimbStairsBU(idx + 2, arr)

    return arr[idx] + min(stepOne, stepTwo)


# top-down
def minCostClimbStairsTP(idx, arr):
    if idx == 1 or idx == 0:
        return arr[idx]
    if idx < 0:
        return 0;
    stepOne = minCostClimbStairsTP(idx - 1, arr)
    stepTwo = minCostClimbStairsTP(idx - 2, arr)

    return arr[idx] + min(stepOne, stepTwo)


if __name__ == '__main__':
    main()
