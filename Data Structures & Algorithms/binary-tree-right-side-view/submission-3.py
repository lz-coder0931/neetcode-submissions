# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []

        q = deque([root])
        res = []

        while q:
            qlen = len(q)

            for i in range(qlen):
                qnode = q.popleft()
                if i == qlen-1:
                    res.append(qnode.val)
                if qnode.left:
                    q.append(qnode.left)
                if qnode.right:
                    q.append(qnode.right)
        return res


        