import heapq as h
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums=[-x for x in nums]
        h.heapify(nums)
        while k:
            ele=h.heappop(nums)
            k-=1
        return -ele