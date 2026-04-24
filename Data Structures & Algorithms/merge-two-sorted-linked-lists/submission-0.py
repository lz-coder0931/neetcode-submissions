# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ls1, ls2 = list1, list2
        newls = ListNode()
        curr = newls
        # if ls1.val <= ls2.val:
        #     newls = ls1
        # else:
        #     newls
        while ls1 or ls2:
            if ls1 == None:
                curr.next = ls2
                ls2 = ls2.next
            elif ls2 == None:
                curr.next = ls1
                ls1 = ls1.next
            else:
                if ls1.val <= ls2.val:
                    curr.next = ls1
                    ls1 = ls1.next
                else:
                    curr.next = ls2
                    ls2 = ls2.next
            curr = curr.next
        return newls.next
            
        