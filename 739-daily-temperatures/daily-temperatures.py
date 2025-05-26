class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        # NGE 
        n=len(temp)
        res=[0]*n
        st=[]
        for i in range(n-1,-1,-1):
            while st and temp[st[-1]]<=temp[i]:
                st.pop()
            if st:
                # print(st[-1])
                res[i]=abs(st[-1]-i)
            st.append(i)
            # appending index so i can return no fo days here ddays means indexes 
        return res
