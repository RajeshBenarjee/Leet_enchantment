class Solution:
    def dailyTemperatures(self, arr: List[int]) -> List[int]:
        n=len(arr)
        res=[0]*n
        st=[]
        for i in range(n-1,-1,-1):
            while st and arr[st[-1]]<=arr[i]:
                st.pop()
            if st:
                res[i]=st[-1]-i
            st.append(i)
        return res