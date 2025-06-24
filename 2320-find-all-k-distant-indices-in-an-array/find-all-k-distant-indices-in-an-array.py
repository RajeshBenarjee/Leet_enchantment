class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        # find all the occurences of key O(N)
        # caluclate the mod distance onw by one and add the indicies if true we call it as condi 
        n=len(nums)
        res=set()
        for i in range(n):
            if nums[i]==key:
                # inserting all the range of indicies 
                for j in range(-k, k + 1):
                    idx = i + j
                    if 0 <= idx < n:
                        res.add(idx)
        # set.sorted
        return sorted(res)