class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m,n=len(obstacleGrid),len(obstacleGrid[0])
        dp=[[-1]*(n+1) for _ in range(m+1)]
        def rec(i,j):
            if dp[i][j]!=-1:
                return dp[i][j]
            if i<0 or j<0:
                return 0
            if obstacleGrid[i][j]==1:
                return 0
            if i==0 and j==0:
                return 1
            up=down=0
            if i>0:
                up=rec(i-1,j)
            if j>0:
                down=rec(i,j-1)
            dp[i][j]=up+down
            return dp[i][j]
        return rec(m-1,n-1)