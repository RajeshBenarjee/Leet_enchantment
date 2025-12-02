class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s)!=len(goal):
            return False
        comp=s+s
        n=len(comp)
        m=len(goal)
        for i in range(0,n-m+1):
            slc=comp[i:i+m]
            # print(slc)
            if slc==goal:
                return True
        return False