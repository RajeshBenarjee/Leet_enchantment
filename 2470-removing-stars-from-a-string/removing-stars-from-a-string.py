class Solution:
    def removeStars(self, s: str) -> str:
        listy=[]
        for i in s:
            if listy==[]:
                listy.append(i)
            elif i=='*':
                listy.pop()
            else:
                listy.append(i)
        return "".join(listy)