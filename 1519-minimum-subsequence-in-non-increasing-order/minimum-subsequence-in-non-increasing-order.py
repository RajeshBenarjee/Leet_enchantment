class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        # they asked about the subsequece so i can sort it ?? - yeah u can 
        nums.sort(reverse=True)
        n=len(nums)
        sumi=sum(nums)
        curr_sum=0
        temp=[]
        for i in range(n):
            curr_sum+=nums[i]
            temp.append(nums[i])
            sumi-=nums[i]
            if curr_sum>sumi:
                break
        return temp
            
