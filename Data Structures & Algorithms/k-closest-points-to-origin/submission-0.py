import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        res = []
        pts = defaultdict(list)
        for x, y in points:
            distance = math.sqrt((0 - x)**2 + (0 - y)**2)
            pts[distance].append([x,y])
            heapq.heappush(heap, distance)
        for _ in range(k):
            distance = heapq.heappop(heap)
            res.append(pts[distance][-1])
            pts[distance].pop()
        return res