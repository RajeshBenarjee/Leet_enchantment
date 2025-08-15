class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        # T(N)-> O(N) S(N)->O(1)
        zero=0
        neg=0
        pos=0
        for i in nums:
            if i==0:
                zero+=1
            elif i<0:
                neg+=1
            else:
                pos+=1
        return max(pos,neg)