# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def dfs_normal(node):
            if not node:
                return ['#']
            return [node.val] + dfs_normal(node.left) + dfs_normal(node.right)

        def dfs_mirror(node):
            if not node:
                return ['#']
            return [node.val] + dfs_mirror(node.right) + dfs_mirror(node.left)

        if not root:
            return True

        return dfs_normal(root.left) == dfs_mirror(root.right)