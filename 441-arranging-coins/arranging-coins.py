class Solution:
    def arrangeCoins(self, n: int) -> int:
        # the number of steps completed equal to sum of all the natural numbers opto to there so find the mid find the sum of natural numbers upto mid if the n is < sum of mid move left else right return the high 
        def sumi(n):
            return (n*(n+1))//2
        low=0
        high=n
        while low<=high:
            mid=low+(high-low)//2
            if sumi(mid)>n:
                high=mid-1
            else:
                low=mid+1
        return high