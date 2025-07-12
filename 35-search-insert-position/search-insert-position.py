class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        def binary(arr,low,high,target):
            ans=high+1
            while low<=high:
                mid=low+(high-low)//2
                if arr[mid]>=target:
                    ans=mid
                    high=mid-1
                else:
                    low=mid+1
            return ans
        return binary(nums,0,len(nums)-1,target)