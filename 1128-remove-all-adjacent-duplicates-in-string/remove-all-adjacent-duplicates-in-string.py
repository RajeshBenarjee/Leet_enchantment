
class Solution:
    def removeDuplicates(self, s: str) -> str:
        listy=[]

        for i in s:
            if listy==[]:
                listy.append(i)
            elif listy[-1]==i:
                listy.pop()
            else:
                listy.append(i)

        return ''.join(listy)
        
            

        
        
            