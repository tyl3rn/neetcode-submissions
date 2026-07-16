class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        '''
        [1,2]

        [2,4]

        [5,6]


        '''
        res = 0
        intervals.sort(key=lambda start: start[0])
        curr = intervals[0]
        for i in range(1, len(intervals)):
            if curr[1] <= intervals[i][0]:
                curr = intervals[i]
            else:
                res +=1
                curr[1] = min(intervals[i][1], curr[1])
        return res 
            