class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid:
            return None
        ROWS, COLS = len(grid), len(grid[0])
        directions = ((0, 1), (0, -1), (-1, 0), (1,0))
        queue = deque()
        # O(m * n)
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 0:
                    queue.append((row, col))
        #bfs
        distance = 1
        while queue:
            n = len(queue)
            for _ in range(n):
                r, c = queue.popleft() 
                for dr, dc in directions:
                    ur, uc = r + dr, c + dc
                    if 0 <= ur < ROWS and 0 <= uc < COLS:
                        if grid[ur][uc] == 2147483647:
                            grid[ur][uc] = distance
                            queue.append((ur, uc))
            distance += 1




