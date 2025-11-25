class Solution:
    def maxDepth(self, s: str) -> int:
        maxi=float('-inf')
        cnt=0
        for i in s:
            if i=='(':
                cnt+=1
            elif i==')':
                if cnt==0:
                    pass
                else:
                    cnt-=1
            maxi=max(maxi,cnt)
        return maxi