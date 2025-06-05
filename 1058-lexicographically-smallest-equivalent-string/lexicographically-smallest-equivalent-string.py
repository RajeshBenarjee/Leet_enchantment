class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = {}

        
        for c in set(s1 + s2 + baseStr):
            parent[c] = c
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])  
            return parent[x]
        
        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX < rootY:
                parent[rootY] = rootX
            else:
                parent[rootX] = rootY
        
        for a, b in zip(s1, s2):
            union(a, b)
        
        result = ''
        for c in baseStr:
            result += find(c)
        
        return result
