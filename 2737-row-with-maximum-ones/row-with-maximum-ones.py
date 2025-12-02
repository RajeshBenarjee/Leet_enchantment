from collections import Counter
class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        # brute force 
        maxi=[float('-inf'),float('-inf')]
        for i in range(len(mat)):
            ones=Counter(mat[i])[1]
            # print(ones)
            if maxi[1]<ones:
                maxi[0]=i
                maxi[1]=ones
        return maxi