class Solution:
    def countPrimes(self, n: int) -> int:
        prime=[True for i in range(n)]
        p=2
        while p*p<=n:
            if prime[p]==True:
                for i in range(p*p,n,p):
                    prime[i]=False
            p+=1
        c=0
        for i in range(2,len(prime)):
            if prime[i]:
                # print(i)
                c+=1
        return c
