class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        #grid approach
        res = 0
        visited = set()
        ROWS, COLS = len(grid), len(grid[0])
        def dfs(r, c):
            if grid[r][c] == "0" or (r, c) in visited:
                return 
            visited.add((r, c))
            directions = ((0,1), (0,-1), (1,0), (-1,0))
            for dr, dc in directions:
                nr, nc = r + dr, dc + c
                if 0 <= nr < ROWS and 0 <= nc < COLS:
                    dfs(nr, nc)
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) not in visited and grid[r][c] == "1":
                    dfs(r, c)
                    res += 1
        return res
            