from collections import Counter
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        s=Counter(nums)
        sumi=0
        for i,j in s.items():
            if j==1:
                sumi+=i
        return sumi