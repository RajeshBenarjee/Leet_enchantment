class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        mapp={"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        res = []
        def backtrack(i,ss):
            if i==len(digits):
                res.append("".join(ss))
                return
            for ch in mapp[digits[i]]:
                ss.append(ch)
                backtrack(i+1,ss)
                ss.pop()
        backtrack(0,[])
        return res