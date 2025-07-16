# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(None, head)
        groupprev = dummy
        while True:
            # Get the kth node. we're going to use its next to set as the prev.
            kth = self.getkth(groupprev, k)
            
            if not kth:
                break
            groupNext = kth.next
            prev, curr = groupNext, groupprev.next
            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            # connecting the previou group's last node to the curr start == kth node. 
            tmp = groupprev.next
            groupprev.next = kth
            groupprev = tmp



            
        return dummy.next
    def getkth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k-=1
        return curr
       
        