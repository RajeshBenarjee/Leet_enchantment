import math
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def possible(d,arr,th):
            sumi=0
            for i in arr:
                sumi+=math.ceil(i/d)
            return sumi<=th
        low=1
        high=max(nums)
        while low<=high:
            mid=low+(high-low)//2
            if possible(mid,nums,threshold):
                high=mid-1
            else:
                low=mid+1
        return low