class Solution:
    def longestPalindrome(self, s: str) -> str:
        '''
        Start in center of string then grow outwards.
        '''
        resLen = 0
        resIdx = 0
        for i in range(len(s)):       

            l, r = i, i #odd
            while l>=0 and r<len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    resIdx = l
                    resLen = r - l + 1
                l-=1
                r+=1
            l, r = i, i+1 #odd
            while l>=0 and r<len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    resIdx = l
                    resLen = r - l + 1
                l-=1
                r+=1
        return s[resIdx:resIdx + resLen ]
            


        
