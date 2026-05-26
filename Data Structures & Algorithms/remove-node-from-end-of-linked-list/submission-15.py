# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None

        length = 0
        curr = head 
        while curr:
            curr = curr.next
            length += 1
        if n == length:
            return head.next

        if length == 1 and n == 1:
            head = None
            return head
        i = 0
        curr = head  
        stop = length - n - 1

        while i<stop:
            curr = curr.next
            i+=1
        curr.next = curr.next.next if curr.next else None
        return head 
    


        