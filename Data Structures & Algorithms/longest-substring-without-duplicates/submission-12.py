class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        n = len(s)
        s = "xxxx"
        sliding window approach
        use two pointers 
        left ptr is initialized to 0

        res = 0
        curr = 0

        for r in range(n):


            while loop inside to shrink window if invalid 
            invalid conition is to use a set and check duplicates using set membersdhip
            check s[r] and if thats in sett, remove s[l] and see if that changes anything 

            while s[r] in sett:
                sett.remove(s[l])
                curr -= 1
            sett.add(s[r])
            curr += 1
            #outside of whiel loop
            res = max(res, curr)
        '''

        n = len(s)
        l = 0
        res = 0
        curr = 0
        sett = set()
        for r in range(n):

            while s[r] in sett:
                sett.remove(s[l])
                l += 1
            sett.add(s[r])
            res = max(res, r - l + 1)
        return res 
        