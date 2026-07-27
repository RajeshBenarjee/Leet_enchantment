class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[[-1]*(n+1) for _ in range(m+1)]
        def rec(i,j):
            if dp[i][j]!=-1:
                return dp[i][j]
            if i==0 and j==0:
                return 1
            if i<0 or j<0:
                return 0
            up=rec(i-1,j)
            down=rec(i,j-1)
            dp[i][j]=up+down
            return dp[i][j]
        return rec(m-1,n-1)