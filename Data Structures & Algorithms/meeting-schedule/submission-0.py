"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        #sort by start time, is curr start time < than prev end time  (if so, invalid)
        sorted_intervals = sorted(intervals, key=lambda x: x.start)
        for i in range(1, len(intervals)):
            if sorted_intervals[i].start < sorted_intervals[i-1].end:
                return False
        return True