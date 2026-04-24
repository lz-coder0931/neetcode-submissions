# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        dic = {}
        while head.next:
            if head not in dic:
                dic[head] = 1
            else:
                return True
            head = head.next
        return False
        