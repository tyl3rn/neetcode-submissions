import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        res = []
        for x, y in points:
            distance = math.sqrt((0 - x)**2 + (0 - y)**2)
            heapq.heappush(heap, [distance, x, y])
        for _ in range(k):
            info = heapq.heappop(heap)
            res.append(info[1:])
        return res