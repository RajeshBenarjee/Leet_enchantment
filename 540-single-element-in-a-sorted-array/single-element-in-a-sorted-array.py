class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # bit manuclation using XOR
        xor=0
        for i in nums:
            xor^=i
        return xor