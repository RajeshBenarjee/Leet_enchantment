class Solution:
    def minOperations(self, logs: List[str]) -> int:
        # T(N)=O(N) S(N)=O(N)
        stacky=[]
        for i in logs:
            if i=="../" and stacky!=[]:
                stacky.pop()
            elif i=="./":
                continue
            elif i!="../" and i!="./":
                stacky.append(i)
            # print(stacky)
        return len(stacky)