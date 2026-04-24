"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # if head is None:
        #     return None
        maptonew = collections.defaultdict(lambda: Node(0))
        maptonew[None] = None

        cur = head
        while cur is not None:
            maptonew[cur].val = cur.val
            maptonew[cur].next = maptonew[cur.next]
            maptonew[cur].random = maptonew[cur.random]
            cur = cur.next
        return maptonew[head]
        