class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Start with n (the length of the array)
        res = len(nums)
        for i in range(len(nums)):
            res ^= (i ^ nums[i])
        return res