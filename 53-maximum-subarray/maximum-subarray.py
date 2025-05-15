class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi=float('-inf')
        s=0
        for  i in nums:
            s+=i
            maxi=max(s,maxi)
            if s<0:
                s=0
        return maxi