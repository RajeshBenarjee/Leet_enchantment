class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        prev=groups[0]
        res=[words[0]]
        for i,j in zip(words,groups):
            if prev==1 and j==0:
                res.append(i)
                prev=j
            elif prev==0 and j==1:
                res.append(i)
                prev=j
        return res
