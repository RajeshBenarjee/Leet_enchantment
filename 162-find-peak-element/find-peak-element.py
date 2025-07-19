class Solution:
    def findPeakElement(self, arr: List[int]) -> int:
        n=len(arr)
        if len(arr)==1:return 0
        if arr[0]>arr[1]:return 0
        if arr[-1]>arr[-2]:return n-1
        low=1
        high=n-2
        while low<=high:
            mid=low+(high-low)//2
            if arr[mid-1]<arr[mid]>arr[mid+1]:
                return mid
            elif arr[mid-1]<arr[mid]:
                # increasing slope so peak is in right eliminate left half 
                low=mid+1
            else:
                high=mid-1
        