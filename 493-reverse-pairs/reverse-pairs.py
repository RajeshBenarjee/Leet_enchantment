class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def count(arr,low,mid,high):
            right=mid+1
            cnt=0
            for i in range(low,mid+1):
                while right<=high and 2*arr[right]<arr[i]:
                    right+=1
                cnt+=(right-(mid+1))
            return cnt
        def merge(arr,low,mid,high):
            cnt=0
            left=low
            right=mid+1
            res=[]
            while left<mid+1 and right<high+1:
                if arr[left]<=arr[right]:
                    res.append(arr[left])
                    left+=1
                else:
                    res.append(arr[right])
                    right+=1

            while left<mid+1:
                res.append(arr[left])
                left+=1
            while right<high+1:
                res.append(arr[right])   
                right+=1

            for i in range(len(res)):
                arr[low + i] = res[i]


        def mergesort(arr,low,high):
            cnt=0
            if low<high:
                mid=(low+high)//2
                cnt+=mergesort(arr,low,mid)
                cnt+=mergesort(arr,mid+1,high)
                cnt+=count(arr,low,mid,high)
                merge(arr,low,mid,high)
            return cnt
        return mergesort(nums,0,len(nums)-1)