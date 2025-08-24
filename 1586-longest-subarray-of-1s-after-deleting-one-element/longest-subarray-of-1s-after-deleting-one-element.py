class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zeros=0
        l=0
        maxi=float('-inf')
        n=len(nums)
        for i in range(n):
            if nums[i]==0 and zeros>=1:  
                while nums[l]!=0:
                    l+=1
                l+=1
            elif nums[i]==1:
                pass
            elif nums[i]==0 and zeros==0:
                zeros+=1
                pass
            temp=i-l
            maxi=max(maxi,temp)
        # print(i,l)
        return maxi