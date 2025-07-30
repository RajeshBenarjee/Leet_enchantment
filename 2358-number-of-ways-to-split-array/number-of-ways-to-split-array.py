class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        # def valid? prefix sum second consiton will take O(N) and for evenry element we can't make o(N) for checking so we moke non zero count indexer
        #  so i need to traverse in reverse to maintain a non zero counter
        # prefix sum
        total_sum = sum(nums)
        prefix_sum = 0
        count = 0
        
        for i in range(len(nums) - 1):
            prefix_sum += nums[i]
            if prefix_sum >= total_sum - prefix_sum:
                count += 1
        return count