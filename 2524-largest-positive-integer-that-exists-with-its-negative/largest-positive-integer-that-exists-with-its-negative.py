class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        l=0
        r=len(nums)-1
        while l<r:
            if (-1*nums[l])==nums[r]:
                print(nums[l],nums[r])
                return abs(nums[l])
            elif abs(nums[l])<nums[r]:
                r-=1
            else:
                l+=1
        return -1