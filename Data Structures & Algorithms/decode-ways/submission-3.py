class Solution:
    def numDecodings(self, s: str) -> int:
        memo = [0 for i in range(len(s)+1)]
        #goes from index 0 to len(s)
        memo[0] = 1
        memo[1] = 1 if s[0] != "0" else 0
        #start from 2, idx0 & 1 are pre-filled

        for i in range(2, len(s)+1):
            ## the "stands alone" case → (prefix)(single)
            if s[i-1] != "0":
                memo[i] = memo[i-1]
                
            #the group as whole case 
            if s[i-2] == "1" or (s[i-2] == "2" and s[i-1] in "0123456"):
                memo[i] += memo[i-2]
    
        return memo[-1]
