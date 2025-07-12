class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary(arr,low,high,target):
            while low<=high:
                mid=low+(high-low)//2
                if arr[mid]==target:
                    return mid
                elif arr[mid]<target:
                    low=mid+1
                else:
                    high=mid-1
            return -1
        return binary(nums,0,len(nums)-1,target)