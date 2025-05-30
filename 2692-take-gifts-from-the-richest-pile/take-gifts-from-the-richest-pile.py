import heapq as h
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        s = [-gift for gift in gifts]
        h.heapify(s)
        for _ in range(k):
            x = -h.heappop(s)
            temp = int(x**0.5)
            h.heappush(s, -temp)
        return -sum(s)

