class Solution:
    def isPerfectSquare(self, n: int) -> bool:
        l=0
        r=n
        while l<=r:
            mid=(l+r)//2
            if mid*mid==n:
                return True
            elif mid*mid>n:
                r=mid-1
            else:
                l=mid+1
        return False