# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        #we dont need middle node, it's included in first half 
        second = slow.next
        slow.next = None
         
        prev = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        curr = head

        while prev:
            tmp1 = curr.next
            tmp2 = prev.next

            curr.next = prev
            prev.next = tmp1

            curr = tmp1
            prev = tmp2



