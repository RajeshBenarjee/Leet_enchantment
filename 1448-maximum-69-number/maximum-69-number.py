class Solution:
    def maximum69Number (self, num: int) -> int:
        # on the way of of traversing if 6 is make it as 9
        snum=str(num)
        n=len(snum)
        cnt=1
        res=''
        for i in range(n):
            if snum[i]=='6' and cnt==1:
                cnt+=1
                res+='9'
            else:
                res+=snum[i]
        return int(res)