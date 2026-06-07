class MedianFinder:

    def __init__(self):
        #left side
        self.maxHeap = []
        #right side 
        self.minHeap = []

    def addNum(self, num: int) -> None:
        #push item to maxHeap by default
        heapq.heappush(self.maxHeap, -num)
        #check if item violates leftside <= rightside
        if (self.maxHeap and self.minHeap) and (-self.maxHeap[0]>self.minHeap[0]):
            value = -heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, value)
    
        #validate lengths of both heaps after potentially moving elements in above condition

        #maxHeap has 2 more elements
        if len(self.maxHeap) > len(self.minHeap)+1:
            value = -heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, value)
        #minHeap has 2 more elements
        if len(self.minHeap) > len(self.maxHeap)+1:
            value = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -value)

    def findMedian(self) -> float:
        if not self.maxHeap and not self.minHeap:
            return 0.0
        if len(self.maxHeap) == len(self.minHeap):
            val1 = -self.maxHeap[0]
            val2 = self.minHeap[0]
            return (val1 + val2) / 2
        elif len(self.maxHeap) > len(self.minHeap):
            return -self.maxHeap[0]
        else:
            return self.minHeap[0]
        
        