class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tMap = defaultdict(int)
        windowMap = defaultdict(int)
        l = 0
        res = ""
        for char in t:
            tMap[char] +=1
        have, need = 0, len(tMap)
        for r in range(len(s)):
            windowMap[s[r]] +=1
            if s[r] in tMap and (windowMap[s[r]] == tMap[s[r]]):
                have+=1
            while have == need:
                if not res or (r-l+1) < len(res):
                    res = s[l:r+1]
                if s[l] in tMap and (windowMap[s[l]] == tMap[s[l]]):
                    have -= 1
                windowMap[s[l]] -=1
                l+=1
        return res
                        