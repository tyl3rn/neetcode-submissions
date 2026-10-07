class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return None
        ROWS, COLS = len(board), len(board[0])
        directions = ((1, 0), (-1,0), (0,1),(0,-1))
        def dfs(r, c):
            if board[r][c] == 'X' or board[r][c] == '-1':
                return
            board[r][c] = '-1'
            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if 0 <= nr < ROWS and 0 <= nc < COLS:
                    dfs(nr, nc)

        for row in range(ROWS):
                for col in range(COLS):
                    if col == 0 or col == COLS - 1 or row == 0 or row == ROWS - 1:
                        if board[row][col] == 'O':
                            dfs(row, col)
        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == 'O':
                    board[row][col] = 'X'
                elif board[row][col] == '-1':
                    board[row][col] = 'O'
             