class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()
        res = []
        rows, cols = len(heights), len(heights[0])
        def dfs(row, col, sett, prev):
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return
            height = heights[row][col]
            if height < prev:
                return 
            if (row, col) in sett:
                return
            sett.add((row, col))
            dfs(row-1, col, sett, height)
            dfs(row+1, col, sett, height)
            dfs(row, col-1, sett, height)
            dfs(row, col+1, sett, height)
        for row in range(rows):
            for col in range(cols):
                if col == 0 or row == 0:
                    dfs(row, col, pacific, 0)
                if row == rows - 1 or col == cols - 1:
                    dfs(row, col, atlantic, 0)
        for row in range(rows):
            for col in range(cols):
                if (row, col) in pacific and (row, col) in atlantic:
                    res.append([row,col])
        return res
                
        


