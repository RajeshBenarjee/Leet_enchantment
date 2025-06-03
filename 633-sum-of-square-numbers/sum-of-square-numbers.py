import math
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a=0
        b=int(math.sqrt(c))
        while a<=b:
            curr=(a*a)+(b*b)
            if curr==c:
                return True 
            elif curr<c:
                a+=1
            elif curr>c:
                b-=1
        return False
