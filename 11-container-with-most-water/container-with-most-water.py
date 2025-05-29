class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        max_a=float('-inf')
        while(l<r):
            h=min(height[l],height[r])
            a=r-l
            area=a*h
            max_a=max(max_a,area)

            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return max_a


