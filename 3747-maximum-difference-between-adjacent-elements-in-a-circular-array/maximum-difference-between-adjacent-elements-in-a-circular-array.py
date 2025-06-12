class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        # as the constraints are small we can use brute force approach 
        maxi=0
        n=len(nums)
        for i in range(n):
            if i==n-1:
                diff=abs(nums[i]-nums[0])
            else:
                diff=abs(nums[i]-nums[i+1])
            if maxi<diff:
                maxi=diff
        return maxi