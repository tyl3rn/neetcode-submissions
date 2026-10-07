class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        ROWS, COLS = len(grid), len(grid[0])
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        res = 0
        def dfs(r, c):
            if grid[r][c] != 1:
                return 0
            grid[r][c] = -1
            maxAround = 0
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS:
                    curr = dfs(nr, nc)
                    maxAround += curr
            return 1 + maxAround
        for row in range(ROWS):
            for col in range(COLS):
                curr = dfs(row, col)
                res = max(res, curr)

        return res