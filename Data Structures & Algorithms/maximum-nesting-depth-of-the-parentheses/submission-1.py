class Solution:
    def maxDepth(self, s: str) -> int:
        res = 0
        curRes = 0
        for char in s:
            if char == "(":
                curRes +=1
                res = max(curRes, res)
            else:
                if char == ")":
                    curRes -= 1    
        return res