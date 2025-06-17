class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        indexed_nums = list(enumerate(nums))  
        top_k = sorted(indexed_nums, key=lambda x: x[1], reverse=True)[:k]
        top_k_sorted = sorted(top_k, key=lambda x: x[0])
        return [num for idx, num in top_k_sorted]