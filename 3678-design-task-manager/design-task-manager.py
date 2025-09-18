from typing import List
import heapq

class TaskManager:
    """
    Manages tasks using a max-heap for priority and a hash map for quick lookups.
    """
    def __init__(self, tasks: List[List[int]]):
        self.task_details = {}
        self.priority_queue = []
        for userId, taskId, priority in tasks:
            self.add(userId, taskId, priority)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        if taskId not in self.task_details:
            self.task_details[taskId] = (userId, priority)
            # Use negative priority and taskId for a max-heap
            heapq.heappush(self.priority_queue, (-priority, -taskId, userId))

    def edit(self, taskId: int, newPriority: int) -> None:
        if taskId in self.task_details:
            userId = self.task_details[taskId][0]
            # Lazily update: just add a new entry to the heap and update the map.
            # The old entry in the heap will be ignored by execTop.
            self.task_details[taskId] = (userId, newPriority)
            heapq.heappush(self.priority_queue, (-newPriority, -taskId, userId))

    def rmv(self, taskId: int) -> None:
        if taskId in self.task_details:
            del self.task_details[taskId]

    def execTop(self) -> int:
        while self.priority_queue:
            # Pop the task with the highest priority and taskId
            neg_priority, neg_taskId, userId = heapq.heappop(self.priority_queue)
            taskId = -neg_taskId
            
            # Check if the task is still valid
            if taskId in self.task_details and self.task_details[taskId][0] == userId and self.task_details[taskId][1] == -neg_priority:
                del self.task_details[taskId]
                return userId
        
        return -1