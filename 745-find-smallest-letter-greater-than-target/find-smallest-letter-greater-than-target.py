class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # lower bound -> array should be sorted 
        n=len(letters)
        l=0
        r=n-1
        ans=letters[0]
        while l<=r:
            mid=l+(r-l)//2
            if letters[mid]>target:
                r=mid-1
                ans=letters[mid]
            else:
                l=mid+1
        return ans