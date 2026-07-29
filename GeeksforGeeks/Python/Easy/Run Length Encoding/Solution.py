class Solution:
    def encode(self, s: str) -> str:
        i=0
        res=''
        while i < len(s):
            cnt=1
            j=i+1
            while j<len(s) and s[i]==s[j]:
                cnt+=1
                j+=1
            res+=s[i]+str(cnt)
            i=j
        return res