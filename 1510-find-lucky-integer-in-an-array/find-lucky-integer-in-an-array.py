from collections import Counter
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq=Counter(arr)
        maxi=-1
        for i,j in freq.items():
            if i==j:
                if i>maxi: maxi=i

        return maxi