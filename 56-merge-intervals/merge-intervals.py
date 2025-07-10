class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans=[intervals[0]]
        n=len(intervals)

        for i in range(1,n):
            if ans[-1][1]<intervals[i][0]:#first element of the next interval is not part of this interval last element create a new list 
                ans.append(intervals[i])
            else:
                if ans[-1][1]<intervals[i][1]:
                    ans[-1][1]=intervals[i][1]
        
        return ans