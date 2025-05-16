class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        types=set(candyType)
        n=len(candyType)
        if len(types)<=(n//2):
            return len(types)
        else:
            return n//2