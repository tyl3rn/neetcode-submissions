class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1 for i in range(n)]
        newRow = [1 for i in range(n)]
        ROWS, COLS = m, n
        for r in range(ROWS-1):
            for c in range(COLS-2,-1, -1):
                newRow[c] = row[c] + newRow[c+1]
            row = newRow

        return newRow[0]
                
