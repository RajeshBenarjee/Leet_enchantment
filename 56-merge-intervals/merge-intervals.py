class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans=[]
        # sort
        intervals.sort()
        # check
        for i  in intervals:
            if ans==[] or ans[-1][1]<i[0]:
                ans.append(i)
            else:
                ans[-1][-1]=max(i[1],ans[-1][-1])
        # return 
        return ans