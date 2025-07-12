# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        curr = dummy
        for i in range(left-1):
            curr = curr.next
        
        res = curr
        curr = curr.next
        rev = curr
        prev = None
        last = None
        # reverse
        for i in range(right-left+1):
            last = rev.next
            rev.next = prev
            prev = rev
            rev = last
        curr.next = rev
        res.next = prev
        return dummy.next
        


        
        
        
