class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[]
        for i in range(n):
            # print(nums[nums[i]])
            res.append(nums[nums[i]])
        return res