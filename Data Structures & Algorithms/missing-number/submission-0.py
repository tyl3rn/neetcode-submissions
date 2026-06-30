class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Start with n (the length of the array)
        res = len(nums)
        
        # XOR every index and every number together
        for i, num in enumerate(nums):
            res ^= i ^ num
            
        return res
