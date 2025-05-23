class Solution:
    def tribonacci(self, n: int) -> int:
        memo={}
        def rec(n):
            if n in memo:
                return memo[n]
            if n==0:
                return 0
            if n==1:
                return 1
            if n==2:
                return 1
            else:
                result=rec(n-1)+rec(n-2)+rec(n-3)

            memo[n]=result
            return result

        return rec(n)