# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        left = float('-inf')
        right = float('inf')
        return self.valid(root, left, right)

    def valid(self, node: Optional[TreeNode], left, right) -> bool:
        if node is None:
            return True
        if not (left< node.val < right):
            return False
        return self.valid(node.left, left, node.val) and self.valid(node.right, node.val, right)



