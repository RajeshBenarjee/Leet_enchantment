class Solution:
    def diagonalSum(self, nums: List[List[int]]) -> int:
        n=len(nums)
        sumi=0
        if n&1==1:
            for i in range(n):
                sumi+=nums[i][n-i-1]
                sumi+=nums[i][i]
            return sumi-nums[n//2][n//2]
        else:
            for i in range(n):
                sumi+=nums[i][n-i-1]
                sumi+=nums[i][i]
            return sumi