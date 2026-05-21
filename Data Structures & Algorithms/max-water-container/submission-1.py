class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        maxArea = 0
        l, r = 0, len(heights) - 1

        while l < r:
            maxArea = max(min(heights[l], heights[r]) * (r - l), maxArea)
            if heights[r] > heights[l]:
                l+=1
            else:
                r-=1
        return maxArea