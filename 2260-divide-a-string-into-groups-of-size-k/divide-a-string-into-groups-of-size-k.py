class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        res=[]
        s_copy=s[:]
        n=len(s)
        if n%k!=0:
            num=n//k+1
            fill_k=(num*k)-n
            s_copy+=f'{fill}'*fill_k
        n_n=len(s_copy)
        for i in range(0,n_n-k+1,k):
            temp=s_copy[i:i+k]
            res.append(temp)
        return res