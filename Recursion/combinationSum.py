def main():
    arr = [2, 3, 6, 7]
    arr = [10, 1, 2, 7, 6, 1, 5]
    print(combinationSumOne([], 0, 7, arr, []))
    print('-------------------------------------------')

    print(removeDup(combinationSumTwo([], 0, 27,
                                      [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [])))
    empty = set()
    # print(combinationSumTwoSet(empty, 0, 8, arr, []))


def combinationSumOne(empty, idx, target, arr, final):
    if idx >= len(arr):
        if target == 0:
            final.append(list(empty))
    elif target < 0:
        return
    else:
        empty.append(arr[idx])
        target -= arr[idx]
        combinationSumOne(empty, idx, target, arr, final)
        empty.pop()
        target += arr[idx]
        combinationSumOne(empty, idx + 1, target, arr, final)
    return final


def combinationSumTwo(empty, idx, target, arr, final):
    if idx >= len(arr):
        if target == 0:
            final.append(sorted(list(empty)))
    elif target < 0:
        return
    else:
        empty.append(arr[idx])
        target -= arr[idx]
        combinationSumTwo(empty, idx + 1, target, arr, final)
        empty.pop()
        target += arr[idx]
        combinationSumTwo(empty, idx + 1, target, arr, final)
    return sorted(final)


def removeDup(array):
    if len(array) == 1:
        return array
    limit = len(array)
    x = 0
    count = 0
    while (x < limit - 1 - count):
        if array[x] == array[x + 1]:
            array.remove(array[x + 1])
            count += 1
        else:
            x += 1

    return array


def combinationSumTwoSet(empty, idx, target, arr, final):
    '''if idx >= len(arr):
        if target == 0:
            final.append(list(empty))
    elif target < 0:
        return
    else:
        empty.add(arr[idx])
        target -= arr[idx]
        combinationSumTwoSet(empty, idx + 1, target, arr, final)
        empty.pop()
        target += arr[idx]
        combinationSumTwoSet(empty, idx + 1, target, arr, final)
    return sorted(final)'''
    pass


if __name__ == '__main__':
    main()
