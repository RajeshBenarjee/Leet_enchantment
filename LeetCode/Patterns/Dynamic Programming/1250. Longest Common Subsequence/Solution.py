class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1,n2=len(text1),len(text2)
        dp=[[-1]*(n2+1) for _ in range(n1+1)]
        def rec(i1,i2):
            if i1<0 or i2<0:
                return 0
            if dp[i1][i2]!=-1:
                return dp[i1][i2]
            if text1[i1]==text2[i2]:
                dp[i1][i2]= 1+rec(i1-1,i2-1)
                return dp[i1][i2]
            else:
                dp[i1][i2]=0+max(rec(i1-1,i2),rec(i1,i2-1))
                return dp[i1][i2]
        return rec(n1-1,n2-1)