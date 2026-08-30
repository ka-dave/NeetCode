# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        curr1 = head
        lenght = 0

        while curr1:
            lenght += 1
            curr1 = curr1.next
        
        if lenght == 1:
            return
        
        half = lenght // 2

        curr = head
        for i in range(half):
            prev = curr
            curr = curr.next
        prev.next = None

        before = None
        temp = curr

        while temp:
            after = temp.next
            temp.next = before
            before = temp
            temp = after

        temp = ListNode(-1)
        curr = temp
        curr1 = head
        curr2 = before
        while curr1 or curr2:
            if curr1:
                curr.next = curr1
                curr1 = curr1.next
                curr = curr.next
            if curr2:
                curr.next = curr2
                curr2 = curr2.next
                curr = curr.next
        # curr.next = None

        
