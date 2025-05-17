class Solution:
    def reverseWords(self, s: str) -> str:
        words=list(s.split())               #--->o(n)
        res=""
        res+=words[-1]
        for i in range(len(words)-2,-1,-1):
            res+=' '
            res+=words[i]
        return res
        # T(N)=O(N)
        # S(N)=O(N)