class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        shetty_nums = set(nums)
        maxi = 0 
        for i in shetty_nums:
            if i - 1 not in shetty_nums:
                count = 1
                current_num = i
                while current_num + 1 in shetty_nums:
                    count += 1
                    current_num += 1
                maxi = max(maxi, count)
        return maxi
