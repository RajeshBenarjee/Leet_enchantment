class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # find the lower bound 
        low=0
        n=len(nums)
        high=n-1
        ans=n
        while low<=high:
            mid=low+(high-low)//2
            if nums[mid]>=target:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans