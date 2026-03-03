class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        def back(i,n,target,stru):
            if target == 0:
                res.append(stru[:])
                return
            
            if i >= n or target < 0:
                return
            
            stru.append(candidates[i])
            target-=candidates[i]
            back(i,n,target,stru)
            stru.pop()
            target+=candidates[i]
            back(i+1,n,target,stru)
        back(0,len(candidates),target,[])
        return res
