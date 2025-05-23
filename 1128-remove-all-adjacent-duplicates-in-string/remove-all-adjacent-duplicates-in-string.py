
class Solution:
    def removeDuplicates(self, s: str) -> str:
        listy=[s[0]]

        for i in range(1,len(s)):
            if listy==[]:
                listy.append(s[i])
            elif listy[-1]==s[i]:
                listy.pop()
            else:
                listy.append(s[i])
        return ''.join(listy)
        
            

        
        
            