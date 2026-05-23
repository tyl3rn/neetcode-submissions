class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashMap = {']': '[', ')':'(','}':'{'}
        for c in s:
            if c in hashMap:
                if not stack or stack.pop() != hashMap[c]:
                    return False
            else:
                stack.append(c)
        return False if stack else True