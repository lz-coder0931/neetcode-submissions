# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ### dfs
        self.res = 0
        maxnode = root.val
        def dfs(root, maxnode):
            if root.val >= maxnode:
                self.res += 1
            if root.left:
                dfs(root.left, max(maxnode, root.val))
            if root.right:
                dfs(root.right, max(maxnode, root.val))
        dfs(root, maxnode)
        return self.res
        