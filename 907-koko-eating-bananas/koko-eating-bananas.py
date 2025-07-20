import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can_complete(k):
            sumi=0
            for i in piles:
                sumi+=math.ceil(i/k)
            if sumi<=h:
                return True
            return False                
            
        low=1
        high=max(piles)
        ans=high
        while low<=high:
            mid=low+(high-low)//2
            if can_complete(mid):
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return low