from collections import Counter
class Solution:
    def maxDifference(self, s: str) -> int:
        s=Counter(s)
        mini_even=float('inf')
        maxi_odd=float('-inf')
        for i,j in s.items():
            if j&1==1:
                if j>maxi_odd:
                    maxi_odd=j
            else:
                if j<mini_even:
                    mini_even=j
        return maxi_odd-mini_even
            
