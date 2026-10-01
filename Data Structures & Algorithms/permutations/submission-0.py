class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        def backtrack(i, path):
            if len(path) == len(nums):
                res.append(path[:])
            for j in range(0, len(nums)):
                if nums[j] in path:
                    continue
                #make choice
                path.append(nums[j])
                backtrack(j, path)
                path.pop()
        backtrack(0, path)
        return res
