from collections import deque
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited=set()
        q=deque([0])

        while q:
            curr=q.popleft()
            visited.add(curr)

            for key in rooms[curr]:
                if key not in visited:
                    q.append(key)
            
        return len(visited)==len(rooms)