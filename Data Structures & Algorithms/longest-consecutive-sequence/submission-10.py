class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        sett = set(nums)
        res = 0
        for num in nums:
            if (num-1) not in sett:
                i = 0
                while num+i in sett:
                    i+=1
                res = max(i, res)
        return res
                    