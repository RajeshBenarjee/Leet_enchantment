# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        node=root
        if root==None:
            root=TreeNode(val)
            return root
        while root:
            if root.val>val:
                if root.left==None:
                    root.left=TreeNode(val)
                    break
                else:
                    root=root.left
            if root.val<val:
                if root.right==None:
                    root.right=TreeNode(val)
                    break
                else:
                    root=root.right
        return node