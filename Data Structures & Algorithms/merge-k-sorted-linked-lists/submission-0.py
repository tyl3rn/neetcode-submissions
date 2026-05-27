# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = [(l.val, i, l) for i, l in enumerate(lists) if l]
        heapq.heapify(heap)
        dummy = ListNode()
        curr = dummy
        while heap:
            tuplee = heapq.heappop(heap)
            node = tuplee[2]
            index = tuplee[1]
            curr.next = node
            if node.next:
                heapq.heappush(heap, (node.next.val,index,node.next))           
            curr = curr.next
        return dummy.next

            
