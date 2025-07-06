class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # mooore's majority algorithm 
        count=0
        for i in nums:
            if count==0:
                maj=i
            if maj==i:
                count+=1
            else:
                count-=1
        return maj