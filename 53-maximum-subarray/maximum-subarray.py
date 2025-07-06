class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi=float('-inf')
        s=0
        for  i in nums:
            s+=i
            maxi=max(s,maxi)
            if s<0:
                s=0
        return maxi

        # if we want to find the beggining and ending indexes we just keep the temp_start at when we set at zero and increment temp end at every iteration and update at maxi if the curren len > maxi indexes