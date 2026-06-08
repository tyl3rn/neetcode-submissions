class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(index, path, curSum):
            #base cases, when a path is valid or when a path is invalid
            if curSum > target:
                return
            if curSum == target:
                res.append(path[:])
            

            for i in range(index, len(nums)):
                #make choice
                path.append(nums[i])
                #backtrack
                backtrack(i, path, curSum + nums[i])
                #undo
                path.pop()
        backtrack(0, [], 0)
        return res
            