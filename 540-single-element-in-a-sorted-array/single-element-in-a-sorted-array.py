class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # check for the single array element 
        n=len(nums)
        if n==1:
            return nums[0]
        # edge cases for removing additional conditional statments & for first element 
        if nums[0]!=nums[1]:
            return nums[0]
        # edge cases for removiong additional conditional statments & for last element 
        if nums[-1]!=nums[-2]:
            return nums[-1]
        low=1
        high=n-1
        while low<=high:
            mid=low+(high-low)//2
            # check the mid element is single or not 
            if nums[mid-1]!=nums[mid] and nums[mid]!=nums[mid+1]:
                return nums[mid]
            else:
                # check for the elimination cases 
                if mid&1:
                    #it means the mid is odd index so mid-1 should contain the same element and we are standing on the left half should search on the right half ELSE we are standing on the right half should search the left half
                    if nums[mid-1]==nums[mid]:
                        low=mid+1
                    else:
                        high=mid-1
                else:
                    if nums[mid-1]==nums[mid]:
                        high=mid-1
                    else:
                        low=mid+1
            