def main():
    arr = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    print(MaxSumNonAdjacentElements(len(arr)-1, arr, 0, 0))


def MaxSumNonAdjacentElements(idx, arr, take, dont_take):
    if idx == 0:
        return arr[idx]
    if idx < 0:
        return 0
    take = arr[idx] + MaxSumNonAdjacentElements(idx - 2, arr, take, dont_take)
    dont_take = MaxSumNonAdjacentElements(idx-1, arr, take, dont_take)
    return max(take, dont_take)


if __name__ == '__main__':
    main()
