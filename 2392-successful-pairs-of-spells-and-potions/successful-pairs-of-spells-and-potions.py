class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        def binary(arr,low,high,tar,i):
            while low<=high:
                mid=low+(high-low)//2
                if (arr[mid]*i)>=tar:
                    high=mid-1
                else:
                    low=mid+1
            return low if low != -1 else 0
        res=[]
        n=len(potions)
        for i in spells:
            ans=binary(potions,0,n-1,success,i)
            res.append(n-ans)
        return res