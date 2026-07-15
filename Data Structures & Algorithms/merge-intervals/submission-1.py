class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key = lambda i: i[0])
        curr = intervals[0]
        res = []

        # [1,2] ,  [3, 4]
        for i in range(1, len(intervals)):
            if curr[1] < intervals[i][0]:
                res.append(curr)
                curr = intervals[i]
            else:
                curr[1] = max(curr[1], intervals[i][1])
        res.append(curr)
        return res