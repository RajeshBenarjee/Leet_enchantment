import bisect
class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        count = 0
        i = 0

        while i < n:
            right = bisect.bisect_right(nums, nums[i] + k)
            count += 1
            i = right
        return count