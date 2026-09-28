class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        count = 0
        minutes = 0
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque([])
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r, c))
                if grid[r][c] == 1:
                    count += 1
        while queue:
            n = len(queue)
            ogcount = count
            for i in range(n):
                row, col = queue.popleft()
                #validate bounds, then check w
                if row + 1 < ROWS:
                    if grid[row + 1][col] == 1:
                        grid[row + 1][col] = 2
                        count -= 1
                        queue.append((row+1,col))
                if row - 1 >= 0:
                    if grid[row - 1][col] == 1:
                        grid[row - 1][col] = 2
                        count -= 1
                        queue.append((row-1,col))
                if col + 1 < COLS:
                    if grid[row][col+1] == 1:
                        grid[row][col+1] = 2
                        count -= 1
                        queue.append((row,col+1))
                if col - 1 >= 0:
                    if grid[row][col-1] == 1:
                        grid[row][col-1] = 2
                        count -= 1
                        queue.append((row,col-1))
            if count != ogcount:
                minutes += 1
        return minutes if count == 0 else -1
