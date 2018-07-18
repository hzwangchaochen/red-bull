class Solution:
    """
    @param: board: board a 2D board containing 'X' and 'O'
    @return: nothing
    """

    def surroundedRegions(self, board):
        if board is None or len(board) <= 1 or len(board[0]) <= 1:
            return
        m = len(board)
        n = len(board[0])
        for i in range(m):
            self.fill_board(board, i, 0)
            self.fill_board(board, i, n - 1)

        for j in range(n):
            self.fill_board(board, 0, j)
            self.fill_board(board, m - 1, j)
        for i in range(m):
            for j in range(n):
                if board[i][j] == "#":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"

    def fill_board(self, board, i, j):
        if board[i][j] != "O":
            return
        board[i][j] = "#"
        m = len(board)
        n = len(board[0])
        q = [(i, j)]
        while len(q) > 0:
            coord = q.pop(0)
            if coord[0] + 1 < m and board[coord[0] + 1][coord[1]] == "O":
                board[coord[0] + 1][coord[1]] = "#"
                q.append((coord[0] + 1, coord[1]))

            if coord[0] > 0 and board[coord[0] - 1][coord[1]] == "O":
                board[coord[0] - 1][coord[1]] = "#"
                q.append((coord[0] - 1, coord[1]))

            if coord[1] + 1 < n and board[coord[0]][coord[1] + 1] == "O":
                board[coord[0]][coord[1] + 1] = "#"
                q.append((coord[0], coord[1] + 1))

            if coord[1] > 0 and board[coord[0]][coord[1] - 1] == "O":
                board[coord[0]][coord[1] - 1] = "#"
                q.append((coord[0], coord[1] - 1))
