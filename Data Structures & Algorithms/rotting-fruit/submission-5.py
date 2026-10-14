from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        res = 0
        fresh = 0
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
        ROWS, COLS = len(grid), len(grid[0])   
        queue = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1
        while queue and fresh > 0:
            n = len(queue)
            for i in range(n):
                nodeRow, nodeCol = queue.popleft()
                for dr, dc in directions:
                    nr, nc = dr + nodeRow, dc + nodeCol
                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        queue.append((nr, nc))
            res += 1
        return res if fresh == 0 else -1
                    
                