def main():
    nums = [2,1,1,2]
    print(houseRobber(nums, 0))


def houseRobber(arr, idx):
    if idx > len(arr) - 1:
        return 0
    step1 = houseRobber(arr, idx + 2) + arr[idx]
    step2 = houseRobber(arr, idx + 1)
    #rob = max(arr[idx] + houseRobber(arr, idx + 2), houseRobber(arr, idx + 1))
    return max(step1, step2)


if __name__ == '__main__':
    main()
