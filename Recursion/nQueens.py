def main():
    n = 4
    arr = [["."] * n for x in range(n)]
    print(NQueens([], arr, 0, n, set(), set(), set(), arr))


# using sets for no duplicates
def NQueens(result, queens_list, r, n, col, diag1, diag2, arr):
    if r == n:
        copy = ["".join(row) for row in arr]
        return result.append(copy)

    for c in range(n):
        if c in col or (r + c) in diag1 or (r - c) in diag2:
            continue

        arr[r][c] = "Q"
        col.add(c)
        diag1.add(r + c)
        diag2.add(r - c)

        NQueens(result, queens_list, r + 1, n, col, diag1, diag2, arr)

        arr[r][c] = "."
        col.pop()
        diag1.pop()
        diag2.pop()

    return result


def safe():
    # cannot be on the same row
    # cannot be on the same colomn
    # cannot be on the same diagonals
    pass


if __name__ == '__main__':
    main()
