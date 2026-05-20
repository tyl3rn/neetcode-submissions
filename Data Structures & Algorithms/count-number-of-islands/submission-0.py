class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
        Use a dfs (or bfs) helper function. I think either dfs or bfs works.
        Call this helper function on the grid
        Use a loop on some sort. Each time it runs, we want to increment a variable called res 
        Stop once everything is discovered
        Return res
        '''
        #i and j represent the current cell
        def dfs(grid: List[List[str]], i: int, j: int) -> None: 
            stack = [(i,j)] #keeps track of what cell by using its coords as identifying information
            #tuple takes an iterable as an argument, stack = tuple(i, j) doesn't work
            # stack = list((i,j)) won't work also because list takes an iterable and changes it into a list
            while stack:
                i, j = stack.pop()
                if grid[i][j] != '1': #cell is '-1' (discovered already) or a '0'
                    continue
                #mark cell as visited
                grid[i][j] = '-1'
                #BIG: rows and cols are 1-indexed, i and j are 0-indexed 
                if 0 <= (i-1) < rows:
                    stack.append((i-1, j))
                if 0 <= (i+1) < rows:
                    stack.append((i+1, j))
                if 0 <= (j-1) < cols:
                    stack.append((i, j-1))
                if 0 <= (j+1) < cols:
                    stack.append((i, j+1))
                
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        res = 0 
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if grid[i][j] != '1': 
                    continue
                # cell is '1'. 1s are an island (call to dfs to exclude neighbors that are 1s)
                res += 1
                dfs(grid, i, j)
        return res
                                        
                
                    
                