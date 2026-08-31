# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        curr = head
        length = 0

        while curr:
            length += 1
            curr = curr.next

        if length == 1 and n == 1:
            return None
        
        ind = length - n + 1
        
        curr = head
        prev = None
        for _ in range(1,ind):
            prev = curr
            curr = curr.next

        if prev:
            prev.next = curr.next
        else:
            head = head.next
        return head