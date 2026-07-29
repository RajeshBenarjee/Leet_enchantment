class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1,n2=len(text1),len(text2)
        dp=[[-1]*(n2+1) for _ in range(n1+1)]
        def solve(i,j):
            if i>=n1 or j>=n2:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            if text1[i]==text2[j]:
                res=1+solve(i+1,j+1)
            else:
                res=max(solve(i+1,j),solve(i,j+1))
            dp[i][j]=res
            return dp[i][j]
        return solve(0,0)