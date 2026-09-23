class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # to check for presence of a substring in a string, count frequencies
        # of chars (have vs need)
        s1map = defaultdict(int)
        for char in s1:
            s1map[char] += 1
        
        l = 0
        need = len(s1)
        for r in range(len(s2)):
            if s2[l] not in s1map:
                l+=1

            else:
                window = defaultdict(int)
                have = 0
                right = r
                #how to come up with a way to track frequencies? it says abc is in caab which is false but we currently
                #dont track frequencies of specific characters, we only track frequencies of overall characters 
                while right < len(s2) and s2[right] in s1map and window[s2[right]] < s1map[s2[right]]:
                    window[s2[right]] += 1
                    have += 1
                    right += 1
                    if have == need:
                        return True
        return False

