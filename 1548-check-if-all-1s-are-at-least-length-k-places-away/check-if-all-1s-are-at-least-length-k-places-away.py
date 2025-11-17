class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        last_idx = -1
        
        for i, val in enumerate(nums):
            if val == 1:
                if last_idx != -1 and (i - last_idx - 1) < k:
                    return False
                last_idx = i
        
        return True
