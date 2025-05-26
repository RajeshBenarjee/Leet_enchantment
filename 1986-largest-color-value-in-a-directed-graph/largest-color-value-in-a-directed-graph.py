from collections import defaultdict, deque
from typing import List

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        graph = defaultdict(list)
        indegree = [0] * n

        for u, v in edges:
            graph[u].append(v)
            indegree[v] += 1

        count = [[0] * 26 for _ in range(n)]
        queue = deque()

        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)

        visited = 0
        max_color_value = 0

        while queue:
            node = queue.popleft()
            visited += 1
            color_index = ord(colors[node]) - ord('a')
            count[node][color_index] += 1
            max_color_value = max(max_color_value, count[node][color_index])

            for neighbor in graph[node]:
                for c in range(26):
                    count[neighbor][c] = max(count[neighbor][c], count[node][c])
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return max_color_value if visited == n else -1
