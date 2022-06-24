def main():
    arr = [1, 2, 3]
    size = len(arr)
    print(permutationsYT([], arr, []))
    # setArray = set()
    # print(permutationsTwo(setArray, arr, []))
    print(permutationsIB([], [], arr, size))


# TakeUForward Permutations
def permutationsYT(empty, arr, final):
    if len(arr) == 0:
        return final.append(list(empty))
    else:
        for x in range(len(arr)):
            empty.append(arr[x])
            arr_copy = arr.copy()
            arr_copy.remove(arr_copy[x])
            permutationsYT(empty, arr_copy, final)
            empty.pop()
    return final


# InterviewBit Permutations
def permutationsIB(result, perms_list, arr, static_size):
    if len(perms_list) == static_size:
        return result.append(list(perms_list))
    for x in range(len(arr)):
        if arr[x] in perms_list:
            continue
        perms_list.append(arr[x])
        permutationsIB(result, perms_list, arr, static_size)
        perms_list.pop()
    return result


'''
def permutationsTwo(set, arr, final):
    if len(arr) == 0:
        return final.append(list(set))
    else:
        for x in range(len(arr)):
            arr_copy = arr.copy()
            set.add(arr_copy[x])
            arr_copy.remove(arr_copy[x])
            permutationsTwo(set, arr_copy, final)
            set.pop()
    return sorted(final)
'''

if __name__ == '__main__':
    main()
