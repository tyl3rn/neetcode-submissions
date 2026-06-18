class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        res = max(nums)
        curMin, curMax = 1, 1 #neutral numbers, numbers * 1 is the number itself 
        
        for i in range(len(nums)):
            if nums[i] == 0:
                curMin, curMax = 1, 1
                continue
            tmp = curMax * nums[i]
            curMax = max(nums[i]*curMax, nums[i] * curMin, nums[i])
            curMin = min(tmp, nums[i] * curMin, nums[i])
            res = max(res, curMax)
        return res     
            
            
            
        

