class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        def backtracking(i,com):
            if i==len(nums):
                if com[:] not in res:
                    res.append(com[:])
                return
            com.append(nums[i])
            backtracking(i+1,com)
            com.pop()
            backtracking(i+1,com)
        backtracking(0,[])
        return res
