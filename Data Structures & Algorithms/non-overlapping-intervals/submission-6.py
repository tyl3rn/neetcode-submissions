class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda end: end[1])

        curr = intervals[0]
        res = 0
        for i in range(1, len(intervals)):
            if curr[1] <= intervals[i][0]:
                curr = intervals[i]
            else:
                res += 1
                curr[1] = min(curr[1], intervals[i][1])
        return res