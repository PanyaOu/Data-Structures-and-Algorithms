def main():
    #arr = [1,2,3,4,5]
    arr = [1,2,1]
    print(sumSubSeq([], 0, 0, arr, 2, []))

#https://www.youtube.com/watch?v=AxNNVECce8c&list=PLgUwDviBIf0rGlzIn_7rsaR2FQ5e6ZOL9&index=6
#The empty array is the holder of the subsequences from the original array
#We add subSeq to the empty array


#Learn the Take and Not take approach to recursion
def printSubSeq(index, empty, arr):
    if index >= len(arr):
        print(empty)
        return
    empty.append(arr[index])
    printSubSeq(index + 1, empty, arr)
    #empty.remove(arr[index])
    empty.pop()
    printSubSeq(index + 1, empty, arr)

def sumSubSeq(empty, idx, sum, arr, target, final):
    if idx >= len(arr):
        if sum == target:
            final.append(list(empty))
    else:
        empty.append(arr[idx])
        sum += arr[idx]
        sumSubSeq(empty, idx + 1, sum, arr, target, final)
        empty.pop()
        sum -= arr[idx]
        sumSubSeq(empty, idx + 1, sum, arr, target, final)

    return final

if __name__ == '__main__':
    main()
