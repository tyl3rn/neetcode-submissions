class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashMap = {']': '[', ')':'(','}':'{'}
        for c in s:
            if c in hashMap:
                if stack and stack.pop() == hashMap[c]:
                    continue
                else:
                    return False
            else:
                stack.append(c)
        return False if stack else True