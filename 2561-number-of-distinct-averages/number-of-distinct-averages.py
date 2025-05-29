class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        # sorting n logn 
        nums.sort()
        l=0
        r=len(nums)-1
        avg_s=set()
        while l<r:
            t1=nums[l]
            t2=nums[r]
            avg_s.add((t1+t2)/2)
            l+=1
            r-=1
        #     print(t1)
        #     print(t2)
        # print(avg_s)
        return len(avg_s)
