# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        list1 = []
        list2 = []
        dummy = ListNode(-1)
        temp = dummy
        s1 = ''
        s2 = ''

        curr1 = l1
        curr2 = l2

        while curr1:
            e1 = curr1.val
            s1 += str(e1)
            curr1 = curr1.next

        while curr2:
            e2 = curr2.val
            s2 += str(e2)
            curr2 = curr2.next

        ele = int(s1[::-1])+int(s2[::-1])
        for i in str(ele)[::-1]:
            temp.next = ListNode(i)
            temp = temp.next
        return dummy.next
        
        
            

