class Solution:
    def climbStairs(self, n: int) -> int:
        if n >= 0 and n <= 2:
            return n
        res = [-1 for i in range(n+1)]
        res[0] = 0
        res[1] = 1
        res[2] = 2
        for i in range(3, n+1):
            res[i] = res[i-1] + res[i-2]
        return res[n]