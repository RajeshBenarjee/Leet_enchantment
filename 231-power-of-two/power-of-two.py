import math
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if not(n&(n-1))and n>0:
            return True
        return False
        