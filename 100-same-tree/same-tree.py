# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        memo = {}
        
        def dfs(node):
            if node in memo:
                return memo[node]
            if not node:
                return ["#"]
            res = [node.val]
            res += dfs(node.left)
            res += dfs(node.right)
            memo[node] = res
            return res
        
        return dfs(p) == dfs(q)