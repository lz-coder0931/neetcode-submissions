# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        i = 0
        tmpnode = ListNode()
        tmpnode.next = prev
        rev = tmpnode
        if rev.next.next == None:
            return None
        else:
            while i < n-1:
                rev = rev.next
                i+=1
            tmp = rev.next.next
            rev.next.next = None
            rev.next = tmp
        
        prev1, curr1 = None, tmpnode.next

        while curr1:
            temp = curr1.next
            curr1.next = prev1
            prev1 = curr1
            curr1 = temp

        return prev1


