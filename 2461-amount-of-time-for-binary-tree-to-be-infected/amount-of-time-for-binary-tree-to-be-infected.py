# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        ug=defaultdict(list)
        def dfs(node):
            if node.left:
                ug[node.val].append(node.left.val)
                ug[node.left.val].append(node.val)
                dfs(node.left)
            
            if node.right:
                ug[node.val].append(node.right.val)
                ug[node.right.val].append(node.val)
                dfs(node.right)
        dfs(root)
        time=-1
        q=deque([start])
        visited={start}
        while q:
            for i in range(len(q)):
                node=q.popleft()
                for n in ug[node]:
                    if n not in visited:
                        visited.add(n)
                        q.append(n)
            time+=1
        return time 