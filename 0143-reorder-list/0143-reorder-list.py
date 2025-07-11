# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        #reverse the second half of the list, and put them together alternatively

        # 1 -> 2 -> 3 -> 4
        # s,f
        #           second
        # 1 -> 2 -> {3} -> 4 -> 5
        #     s           f
        #               second
        # 1 -> 2 -> 3 -> {4} -> 5-> None
        #          s             f
        slow, fast = head, head.next         
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        
        prev = slow.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        first = head
        second = prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2


