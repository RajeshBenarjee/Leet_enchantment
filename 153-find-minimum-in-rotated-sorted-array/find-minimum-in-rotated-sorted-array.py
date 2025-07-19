class Solution:
    def findMin(self, arr: List[int]) -> int:
        low=0
        high=len(arr)-1
        ans=float('inf')
        while low<=high:
            mid=low+(high-low)//2
            if arr[low]<=arr[mid]:
                # left part is sorted take the arr[low] and move to right part 
                ans=min(ans,arr[low])
                low=mid+1
            elif arr[mid]<=arr[high]:
                # right part is sorted 
                ans=min(ans,arr[mid])
                high=mid-1
        return ans 
                