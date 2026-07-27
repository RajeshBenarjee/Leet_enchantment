class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        dp=[[-1]*(n+1) for _ in range(m+1)]
        def rec(i,j):
            if dp[i][j]!=-1:
                return dp[i][j]
            if i==0 and j==0:
                return grid[0][0]
            if i<0 or j<0:
                return float('inf')

            up=rec(i-1,j)

            down=rec(i,j-1)

            dp[i][j]=grid[i][j]+min(up,down)

            return dp[i][j]

        return rec(m-1,n-1)