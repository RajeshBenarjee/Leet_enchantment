# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def search(root,val):
            if root is None:
                return None
            if root.val==val:
                return root
            if root.val<val:
                # print(root.val)
                return search(root.right,val)
            if root.val>val:
                return search(root.left,val)
        return search(root,val)
            