def main():
    boardTrue = [["5", "3", ".", ".", "7", ".", ".", ".", "."]
        , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
        , [".", "9", "8", ".", ".", ".", ".", "6", "."]
        , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
        , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
        , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
        , [".", "6", ".", ".", ".", ".", "2", "8", "."]
        , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
        , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

    boardFalse = [["8", "3", ".", ".", "7", ".", ".", ".", "."]
        , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
        , [".", "9", "8", ".", ".", ".", ".", "6", "."]
        , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
        , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
        , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
        , [".", "6", ".", ".", ".", ".", "2", "8", "."]
        , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
        , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

    print(isValidSudoku(boardFalse))


def isValidSudoku(board):
    return solve(board)


def solve(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] != ".":
                if isValid(board, i, j, board[i][j]):
                    continue
                return False
    return True


def isValid(board, i, j, char):
    for x in range(9):
        if x != i and board[x][j] == char:
            return False
        if x != j and board[i][x] == char:
            return False
        magicRow = 3 * (i // 3) + x // 3
        MagicCol = 3 * (j // 3) + x % 3
        if magicRow != i and MagicCol != j and board[magicRow][MagicCol] == char:
            return False
    return True


if __name__ == '__main__':
    main()
