class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {}
        for i in range(len(s)):
            lastIndex[s[i]] = i
        output = []
        lastIdx = 0
        res = 0
        for i, n in enumerate(s):
            lastIdx = max(lastIdx, lastIndex[n])
            res+= 1
            if i == lastIdx:
                output.append(res)
                res = 0
        return output
