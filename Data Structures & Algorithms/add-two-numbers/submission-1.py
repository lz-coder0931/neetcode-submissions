# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        result = ListNode(0)
        residue = result
        
        while l1 is not None or l2 is not None:
            carry_on = None
            if l1 is not None:
                if residue.val+l1.val >9:
                    carry_on = ListNode(1)
                residue.val = (residue.val+l1.val) % 10
                l1 = l1.next
            if l2 is not None:
                if residue.val+l2.val >9:
                    carry_on = ListNode(1)
                residue.val = (residue.val+l2.val) % 10
                l2 = l2.next
            if carry_on is None:
                carry_on = ListNode(0)
            if l1 is not None or l2 is not None or carry_on.val == 1:
                residue.next = carry_on
            residue = carry_on
        return result






