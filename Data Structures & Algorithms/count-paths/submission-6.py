class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1 for i in range(n)]
        res = [1 for i in range(n)]
        ROWS, COLS = m, n
        for row in range(ROWS-1):
            for col in range(COLS-2,-1, -1):
                res[col] = dp[col] + res[col+1]
            dp = res

        return res[0]
                
