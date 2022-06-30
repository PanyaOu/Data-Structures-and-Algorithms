def main():
    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    SudokoSolver(board)
    print(board)


def SudokoSolver(board):
    solve(board)

def solve(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == ".":
                for x in range(1, 10):
                    if isValid(board, i, j, str(x)):
                        board[i][j] = str(x)

                        if solve(board):
                            return True
                        else:
                            board[i][j] = "."
                return False

    return True


def isValid(board, i, j, char):
    for x in range(9):
        if board[x][j] == char:
            return False
        if board[i][x] == char:
            return False
        if board[3 * (i // 3) + x // 3][3 * (j // 3) + x % 3] == char:
            return False
    return True


if __name__ == '__main__':
    main()
