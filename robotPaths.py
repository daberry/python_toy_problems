class Board:
    def __init__(self, n):
        board = []
        for i in range(0, n):
            board.append([])
            for j in range(0, n):
                board[i].append(False)

    def togglePiece(self, i, j):
        self[i][j] = not self[i][j]

    def hasBeenVisited(self, i, j):
        return not not self[i][j]

def robotPaths(n, i, j, board):
    if not board:
        board = Board(n)
        i = 0
        j = 0
    if not (i >= 0 and i < n and j >= 0 and j < n) or board.hasBeenVisited(i, j):
        return 0
    if i == n  - 1 and j == n - 1
        return 1
    board.togglePiece(i, j)
    result = robotPaths(n, i, j + 1, board) +
             robotPaths(n, i, j - 1, board) +
             robotPaths(n, i + 1, j, board) +
             robotPaths(n, i - 1, j, board)
    board.togglePiece(i, j)
    return result

