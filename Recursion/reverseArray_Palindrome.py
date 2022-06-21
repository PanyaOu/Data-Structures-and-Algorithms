def main():
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    left = 0
    right = len(array) - 1
    #    reverseArray(left, right,array)
    iterativeReverse(left, right, array)
    print(array)


def reverseArray(left, right, array):
    if left > right:
        return array
    swap(left, right, array)
    reverseArray(left + 1, right - 1, array)


def iterativeReverse(left, right, array):
    while left < right:
        swap(left, right, array)
        left += 1
        right -= 1
    return array


def swap(l, r, arr):
    temp = arr[l]
    arr[l] = arr[r]
    arr[r] = temp


if __name__ == '__main__':
    main()
