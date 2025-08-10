class Solution:
    def reverseWords(self, s: str) -> str:
        n = len(s)
        res = []
        temp = ''
        
        for i in range(n - 1, -1, -1):
            if s[i] == ' ':
                if temp:
                    res.append(temp[::-1])
                    temp = ''
            else:
                temp += s[i]
        
        if temp:
            res.append(temp[::-1])
        
        return ' '.join(res)