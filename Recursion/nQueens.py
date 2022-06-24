def main():
    n = 5
    arr = [["."] * n for x in range(n)]
    print(NQueens([], 0, n, set(), set(), set(), arr))

    '''
    checking specific diagonals
    (r + c)
    [0  1  2  3]
    [1  2  3  4]
    [2  3  4  5]
    [3  4  5  6]
    
    (r - c)
    [0 -1 -2 -3]
    [1  0 -1 -2]
    [2  1  0 -1]
    [3  2  1  0]
    '''


# using sets for no duplicates
def NQueens(result, r, n, col, diag1, diag2, arr):
    if r == n:
        copy = ["".join(row) for row in arr]
        return result.append(copy)

    for c in range(n):
        if c in col or (r + c) in diag1 or (r - c) in diag2:
            continue

        col.add(c)
        # bottom left to top right: constant values
        diag1.add(r + c)
        # top to bottom right: constant values
        diag2.add(r - c)
        arr[r][c] = "Q"

        NQueens(result, r + 1, n, col, diag1, diag2, arr)

        col.remove(c)
        diag1.remove(r + c)
        diag2.remove(r - c)
        arr[r][c] = "."

    return result


def safe():
    # cannot be on the same row
    # cannot be on the same colomn
    # cannot be on the same diagonals
    pass


if __name__ == '__main__':
    main()
