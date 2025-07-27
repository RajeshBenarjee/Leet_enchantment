class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        # O(2N)
        # check for acscending array 
        n=len(nums)
        asc=True
        for i in range(1,n):
            if nums[i-1]>nums[i]:
                asc=False
                break
        # check for descending array
        dsc=True
        for i in range(1,n):
            if nums[i-1]<nums[i]:
                dsc=False
                break
        return asc or dsc