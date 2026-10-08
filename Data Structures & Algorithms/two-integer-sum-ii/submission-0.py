class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        #l = 0, r = 3

#[1,2,3,4], target = 3
# output: 1, 2


        
        while l < r: 
            sumNums = numbers[l] + numbers[r]
            if sumNums == target:
                return [l+1, r+1] #1-indexed so add 1

            elif sumNums < target:
                l+=1
            else:
                r-=1
        