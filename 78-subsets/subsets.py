class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def back(idx,temp):
            if idx>=len(nums):
                res.append(temp[:])
                return 
            temp.append(nums[idx])
            back(idx+1,temp)
            temp.pop()
            back(idx+1,temp)
        back(0,[])
        return res