class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        answer=[]
        n=numRows
        for i in range(1,n+1):
            temp=[1]
            ans=1
            for j in range(1,i):
                ans*=(i-j)
                ans//=(j)
                temp.append(ans)
            answer.append(temp)
        return answer
            