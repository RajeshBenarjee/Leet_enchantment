class Solution:
    def removeStars(self, s: str) -> str:
        listy=[]
        # n=len(s)
        # T(N)=O(N) S(N)=O(N)
        for i in s:
            if listy==[]:
                listy.append(i)
            elif i=='*':
                listy.pop()
            else:
                listy.append(i)
        return "".join(listy)