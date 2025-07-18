class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        def findfirst(nums,target):
            start=-1
            low=0
            high=n-1
            while(low<=high):
                mid=(low+high)//2
                if(nums[mid]==target):
                    start=mid
                    high=mid-1
                elif(nums[mid]>target):
                    high=mid-1
                else:
                    low=mid+1
            return start
        def findlast(nums,target):
            end=-1
            low=0
            high=n-1
            while(low<=high):
                mid=(low+high)//2
                if(nums[mid]==target):
                    end=mid
                    low=mid+1
                elif(nums[mid]>target):
                    high=mid-1
                else:
                    low=mid+1
            return end
        return [findfirst(nums,target),findlast(nums,target)]
