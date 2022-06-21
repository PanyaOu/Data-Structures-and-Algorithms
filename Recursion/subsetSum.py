def main():
    arr = [3,1,2]
    print(subsetSum(0, [], arr, []))

def subsetSum(idx, subset, arr, final):
    if idx > len(arr) - 1:
        final.append(sum(subset))
        return
    else:
        subset.append(arr[idx])
        subsetSum(idx + 1, subset, arr, final)
        subset.pop()
        subsetSum(idx + 1, subset, arr, final)
    return sorted(final)
    


if __name__ == '__main__':
    main()
