class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        # n=len(nums)
        # for i in range(n):
        sumi=0
        for i in range(len(nums)):
            temp=bin(i).count('1')
            if temp==k:
                # print(i)
                sumi+=nums[i]
        return sumi