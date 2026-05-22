class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        res = 0
        mapp = defaultdict(int)
        maxChar = 0
        for r in range(len(s)):
            mapp[s[r]] += 1
            maxChar = max(mapp[s[r]], maxChar)
            while (r-l + 1) - maxChar > k:
                mapp[s[l]] -= 1
                maxChar = max(mapp[s[l]], maxChar)
                l+=1
        return r - l + 1
