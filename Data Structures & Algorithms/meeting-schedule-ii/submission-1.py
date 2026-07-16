import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x.start)
        heap = []  # end times of rooms currently in use
        for iv in intervals:
            if heap and heap[0] <= iv.start:
                heapq.heappop(heap)   # earliest-freeing room is free, reuse it
            heapq.heappush(heap, iv.end)
        return len(heap)