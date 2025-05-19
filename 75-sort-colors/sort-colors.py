class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c=0
        b=len(nums)-1
        p=0
        while(p<=b):
            if nums[p]==0:
                (nums[p],nums[c])=(nums[c],nums[p])
                c+=1
                p+=1
            elif nums[p]==2:
                (nums[p],nums[b])=(nums[b],nums[p])
                b-=1
            elif nums[p]==1:
                p+=1
        
