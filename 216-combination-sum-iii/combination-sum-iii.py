class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []

        def backtrack(start, k, target, temp):
            if k == 0 and target == 0:
                res.append(temp[:])
                return
            
            if target < 0:
                return

            for i in range(start, 10):
                temp.append(i)
                backtrack(i + 1, k - 1, target - i, temp)
                temp.pop()

        backtrack(1, k, n, [])
        return res