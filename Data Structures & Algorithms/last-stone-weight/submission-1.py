class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones:
            return 0
        heap = []

        for stone in stones:
            heapq.heappush(heap,-stone)

        while len(heap) > 1:
            y = -heapq.heappop(heap)
            x = -heapq.heappop(heap)
            if x == y:
                continue
            else:
                heapq.heappush(heap, -(y-x))
        if len(heap) == 0:
            return 0
        else:
            res = -heapq.heappop(heap)
            return res


