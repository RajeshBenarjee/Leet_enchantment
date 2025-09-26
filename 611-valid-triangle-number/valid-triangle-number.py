from typing import List

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        count = 0

        # Fix the largest side (c)
        for k in range(n - 1, 1, -1):
            left, right = 0, k - 1
            while left < right:
                if nums[left] + nums[right] > nums[k]:
                    # All pairs between left and right are valid
                    count += (right - left)
                    right -= 1
                else:
                    left += 1
        return count
        
