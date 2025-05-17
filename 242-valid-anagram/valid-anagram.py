class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        # if set(s)==set(t):
        #     return True
        # return False
        d1={}
        for i in range(len(s)):
            if s[i] in d1:
                d1[s[i]]+=1
            else:
                d1[s[i]]=1
        for i in range(len(t)):
            if t[i] in d1:
                d1[t[i]]-=1
                if d1[t[i]]<0:
                    return False
            else:
                return False
        return True