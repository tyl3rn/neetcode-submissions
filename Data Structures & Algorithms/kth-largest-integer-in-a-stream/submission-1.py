class KthLargest:

    def __init__(self, k: int, nums: List[int]):
       self.num = k
       self.numbers = sorted(nums)
    def add(self, val: int) -> int:
        self.numbers.append(val)
        self.numbers.sort()
        res = None
        return self.numbers[len(self.numbers) - self.num]