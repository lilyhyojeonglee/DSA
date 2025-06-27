# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        count = 1
        while curr.next:
            curr = curr.next
            count +=1
        curr = head
        remove = count - n
        if remove == 0:
            return head.next
    
        for i in range( remove-1):
            curr = curr.next
        curr.next = curr.next.next
        return head