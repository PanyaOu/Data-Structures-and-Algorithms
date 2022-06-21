def main():
    arr = [1, 2, 3]
    print(permutations([], arr, []))
    # setArray = set()
    # print(permutationsTwo(setArray, arr, []))


def permutations(empty, arr, final):
    if len(arr) == 0:
        return final.append(list(empty))
    else:
        for x in range(len(arr)):
            empty.append(arr[x])
            arr_copy = arr.copy()
            arr_copy.remove(arr_copy[x])
            permutations(empty, arr_copy, final)
            empty.pop()
    return final


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
