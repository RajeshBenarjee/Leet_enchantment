class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ind=-1
        for i in range(len(nums)-2,-1,-1):
            if(nums[i]<nums[i+1]):
                ind=i
                break
        if ind==-1:
            return nums.reverse()
        for i in range(len(nums)-1,-1,-1):
            if(nums[ind]<nums[i]):
                (nums[i],nums[ind])=(nums[ind],nums[i])
                break
        nums[ind+1:]=reversed(nums[ind+1:])