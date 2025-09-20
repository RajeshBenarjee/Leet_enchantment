class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        start=[(j[0],i)for i,j in enumerate(intervals)]
        start.sort(key=lambda x:x[0])
        res=[]
        for i in intervals:
            cur_end=i[1]
            left=0
            right=len(start)-1
            ans=-1
            while left<=right:
                mid=(left+right)//2
                if start[mid][0]>=cur_end:
                    ans=start[mid][1]
                    right=mid-1
                else:
                    left=mid+1
            res.append(ans)
        return res
            