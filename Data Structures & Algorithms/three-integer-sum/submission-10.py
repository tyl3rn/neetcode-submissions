class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]: #fixed num is the same 
                continue 
            l, r = i + 1, len(nums) - 1
            while l < r:
                total = nums[l] + nums[r] + nums[i]
                if(total== 0):
                    res.append([nums[l], nums[r], nums[i]])
                    r-=1
                    while l<r and nums[r] == nums[r+1]:
                        r-=1
                elif total > 0:
                    r -= 1
                else:
                    l += 1

        return res
            
