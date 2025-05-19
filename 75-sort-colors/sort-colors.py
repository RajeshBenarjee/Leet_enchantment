class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """    
        # l=0
        # h=0
        # n=len(nums)
        # while(l<=n):
        #     if l==2:
        #         nums.pop(l)
        #         nums.append(2)
        #     elif nums[l]==0:
        #         nums.pop(l)
        #         nums.insert(0,h)
        #         l+=2
        #     else:
        #         l+=1
        

        c_0=0
        c_1=0
        c_2=0
        for i in nums:
            if i==0:
                c_0+=1
            elif i==1:
                c_1+=1
            else:
                c_2+=1
        for i in range(0,c_0):
            nums[i]=0
        for i in range(c_0,c_1+c_0):
            nums[i]=1
        for i in range(c_0+c_1,c_1+c_0+c_2):
            nums[i]=2
    

            