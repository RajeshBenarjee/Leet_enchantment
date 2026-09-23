import heapq as h
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)

        heap = []
        for num, count in freq.items():
            h.heappush(heap, (-count, num))   
            
        res = []
        while k:
            count, num = h.heappop(heap)
            res.append(num)
            k -= 1

        return res