class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        minutes = 0
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque([])
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1
        while queue and fresh > 0:
            n = len(queue)
            for i in range(n):
                row, col = queue.popleft()
                for dr, dc in directions:
                    nr, nc = row + dr, dc + col
                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        queue.append((nr, nc))
            minutes += 1
        return minutes if fresh == 0 else -1
