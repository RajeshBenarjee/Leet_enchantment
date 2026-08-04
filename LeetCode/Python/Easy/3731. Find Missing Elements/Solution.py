class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        start,end=min(nums),max(nums)
        org=set(i for i in range(start,end+1))
        have=set(nums)
        return list(org-have)