class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count=0
        for i in nums:
            n=len(str(i))
            if n&1==0:
                count+=1
        return count