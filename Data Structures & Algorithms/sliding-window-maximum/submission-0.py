class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l, r = 0, 0
        q = deque() #contains indices
        res = []

        while r < len(nums):

            #gets rid of smaller numbers than curr number in queue
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            #keeps front index in range of window 
            if l > q[0]:
                q.popleft()
            
            #if this iteration (adding 1) to r causes window to exceed size k,
            #shift l ptr over and add largest number (left most) to res since we are getting 
            #rid of that in the window 
            if r + 1 >= k:
                res.append(nums[q[0]])
                l+=1
            r+=1
        return res
        
