class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return None
        res = 0
        directions = [(1,0),(-1,0),(0,-1),(0,1)]
        ROWS, COLS = len(grid), len(grid[0])
        def dfs(r: int, c: int) -> None:
            if grid[r][c] != "1":
                return
            grid[r][c] = "-1"
            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if 0 <= nr < ROWS and 0 <= nc < COLS:
                    dfs(nr, nc)
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == "1":
                    dfs(row, col)
                    res += 1
        return res