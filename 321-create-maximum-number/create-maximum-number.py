class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        def max_subsequence(nums, k):
            stack = []
            drop = len(nums) - k
            for num in nums:
                while drop and stack and stack[-1] < num:
                    stack.pop()
                    drop -= 1
                stack.append(num)
            return stack[:k]
        
        def merge(sub1, sub2):
            res = []
            while sub1 or sub2:
                if sub1 > sub2:
                    res.append(sub1.pop(0))
                else:
                    res.append(sub2.pop(0))
            return res
        
        max_num = []
        for i in range(max(0, k - len(nums2)), min(k, len(nums1)) + 1):
            sub1 = max_subsequence(nums1, i)
            sub2 = max_subsequence(nums2, k - i)
            candidate = merge(sub1.copy(), sub2.copy())
            max_num = max(max_num, candidate)
        
        return max_num
