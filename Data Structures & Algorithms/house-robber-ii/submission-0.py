class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0],nums[1])
        
        def robHelp(nums: List[int]) -> int:
            memo = [-1 for i in range(len(nums)+1)]
            memo[0] = 0
            memo[1] = nums[0]
            memo[2] = max(nums[0],nums[1])
            for i in range(3, len(nums)+1):
                memo[i] = max(memo[i-1],(nums[i-1] + memo[i-2]))
        
            return memo[-1]
        return max(robHelp(nums[:-1]), robHelp(nums[1:]))
