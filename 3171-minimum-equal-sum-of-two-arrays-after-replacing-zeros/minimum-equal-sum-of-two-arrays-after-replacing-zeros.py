class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        sum1 = sum(x for x in nums1 if x != 0)
        sum2 = sum(x for x in nums2 if x != 0)
        zero1 = nums1.count(0)
        zero2 = nums2.count(0)

        minSum1 = sum1 + zero1
        minSum2 = sum2 + zero2

        if minSum1 == minSum2:
            return minSum1

        if minSum1 > minSum2:
            diff = minSum1 - minSum2
            if zero2 == 0:
                return -1  
            return minSum1 
        else:
            diff = minSum2 - minSum1
            if zero1 == 0:
                return -1  
            return minSum2 
