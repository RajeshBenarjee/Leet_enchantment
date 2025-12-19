class Solution:
    def reverseWords(self, s: str) -> str:
        def counter(word):
            cnt=0
            for i in word:
                if i in 'aeiou':
                    cnt+=1
            return cnt
        words=s.split()
        cnst=counter(words[0])
        res=''
        res+=words[0]
        for i in range(1,len(words)):
            curr_cnt=counter(words[i])
            if cnst==curr_cnt:
                res+=' '
                res+=words[i][::-1]
                
            else:
                res+=' '
                res+=words[i]
                
        return res