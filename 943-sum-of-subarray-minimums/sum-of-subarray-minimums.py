class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD=10**9+7
        #    nse
        st=[]
        nse=[len(arr)]*len(arr)
        for i in range(len(arr)-1,-1,-1):
            while st and arr[st[-1]]>=arr[i]:
                st.pop()
            if st:
                nse[i]=st[-1]
            st.append(i)

        # pse
        st=[]
        pse=[-1]*len(arr)
        for i in range(len(arr)):
            while st and arr[st[-1]]>arr[i]:
                st.pop()
            if st:
                pse[i]=st[-1]
            st.append(i)

        s=0 # Name error

        # print(pse)
        # print(nse)
        for i in range(0,len(arr)):
            count=(i-pse[i])*(nse[i]-i)
            con=arr[i]*count
            s+=con
        return s%MOD
