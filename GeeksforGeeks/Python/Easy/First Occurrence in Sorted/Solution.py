class Solution:
    def firstSearch(self, arr, k):
        ans=0
        low,high=0,len(arr)-1
        while low<=high:
            mid=low+(high-low)//2
            if arr[mid]>=k:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        if k==arr[ans]:
            return ans
        else:
            return -1