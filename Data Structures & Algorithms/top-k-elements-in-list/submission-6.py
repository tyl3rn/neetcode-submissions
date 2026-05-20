class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        if k <= 0:
            return []
        freq = defaultdict(int)
        for num in nums:
            freq[num] +=1
        arr = [[] for i in range(len(nums)+1)]
        for key, v in freq.items():
            arr[v].append(key)
        res = []
        for i in range(len(arr)-1, -1, -1):
            if len(res) >= k:
                return res
            else:
                res.extend(arr[i])
                
        