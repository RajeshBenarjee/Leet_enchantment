class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n=len(nums)
        sumi=0
        maxi=float('-inf')
        for i in range(n):
            sumi+=nums[i]
            if sumi>maxi:
                maxi=sumi
            if sumi<0:
                sumi=0
            
        return maxi