from typing import List

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        cnt = 0
        zeros = 0
        for num in nums:
            if num == 0:
                zeros += 1
                cnt += zeros
            else:
                zeros = 0
        return cnt
