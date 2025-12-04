class Solution:
    def reverseWords(self, s: str) -> str:
        res=''
        listy=s.split()
        for i in range(1,len(listy)+1):
            res+=listy[-i]
            res+=' '
        return res[:-1]