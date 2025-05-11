class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        # go with sliding window 
        # def check(nums):
        #     for i in nums:
        #         if i%2==0:
        #             return False 
        #     return True
        # n=len(arr)
        # for i in range(0,n-3):
        

        #  Going with brute force as the constraint are less
        f=s=t=0
        n=len(arr)
        for i in range(0,n-2):
            f=arr[i]
            s=arr[i+1]
            t=arr[i+2]
            if f%2!=0 and s%2!=0 and t%2!=0:
                return True
        return False