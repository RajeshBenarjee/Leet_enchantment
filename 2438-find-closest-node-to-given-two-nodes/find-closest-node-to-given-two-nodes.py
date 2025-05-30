from collections import deque
from typing import List

class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        def get_distances(start):
            dist = [-1] * len(edges)
            q = deque([start])
            d = 0
            while q:
                for _ in range(len(q)):
                    node = q.popleft()
                    if dist[node] == -1:
                        dist[node] = d
                        if edges[node] != -1:
                            q.append(edges[node])
                d += 1
            return dist
        
        dist1 = get_distances(node1)
        dist2 = get_distances(node2)
        
        res = -1
        min_dist = float('inf')
        
        for i in range(len(edges)):
            if dist1[i] != -1 and dist2[i] != -1:
                max_dist = max(dist1[i], dist2[i])
                if max_dist < min_dist:
                    min_dist = max_dist
                    res = i
        return res
