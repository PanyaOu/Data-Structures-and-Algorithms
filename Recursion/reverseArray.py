def main():
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

    arrPal = [1, 2, 3, 2, 1]

    # reverseArray(0, len(array)-1 ,array)
    # iterativeReverse(0, len(array)-1 ,array)
    # print(array)
    print(checkPalindrome(0, len(arrPal) - 1, arrPal))


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


def checkPalindrome(left, right, array):
    while (left < right):
        if array[left] == array[right]:
            left += 1
            right -= 1
        else:
            return False
    return True


def swap(l, r, arr):
    temp = arr[l]
    arr[l] = arr[r]
    arr[r] = temp


if __name__ == '__main__':
    main()
