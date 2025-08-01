class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def possible(arr,k,mid):
            count=1
            curr_sumi=0
            n=len(arr)
            for i in range(n):
                if curr_sumi+arr[i]>mid:
                    count+=1
                    curr_sumi=arr[i]
                else:
                    curr_sumi+=arr[i]
            return count
                
        low=max(nums)
        high=sum(nums)
        while low<=high:
            mid=low+(high-low)//2
            if possible(nums,k,mid)<=k:
                high=mid-1
            else:
                low=mid+1
        return low
