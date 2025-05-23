class Solution:
    def kidsWithCandies(self, candies: List[int], extra: int) -> List[bool]:
        n=len(candies)
        res=[True]*n
        maxi=max(candies)
        for i in range(n):
            if extra+candies[i]>=maxi:
                continue
            else:
                res[i]=False
        return res

