class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def back(i, n, stru, sumi):
            
            if sumi == target:
                res.append(stru[:])
                return
            if sumi > target:      # pruning
                return
            
            for ind in range(i, n):
                if ind > i and candidates[ind] == candidates[ind - 1]:
                    continue
                
                stru.append(candidates[ind])
                back(ind + 1, n, stru, sumi + candidates[ind])  # use ind+1
                stru.pop()

        back(0, len(candidates), [], 0)
        return res