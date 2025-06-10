class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result=[]
        def backtrack(i,res):
            # Base Case
            if i==len(nums):
                result.append(res[:])
                return 

            res.append(nums[i]) #inclusion
            backtrack(i+1,res) # step to print inclusion
            res.pop()  # Backtraking step
            backtrack(i+1,res) # step to print exclusion subset

        
        backtrack(0,[])
        return result