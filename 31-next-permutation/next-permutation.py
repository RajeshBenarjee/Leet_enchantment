class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        **This algo has three main steps**

        - First find the nearest drop index (from the right). If no drop, reverse nums.
        - If drop is there, find the smallest element greater than nums[drop] after it and swap.
        - Reverse the remaining part after drop to get the next permutation.
        """
        n = len(nums)
        drop = -1
        
        # Step 1: Find the drop index (first decreasing element from right)
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                drop = i
                break
        
        if drop == -1:
            nums.reverse()
            return
        
        # Step 2: Find the smallest element greater than nums[drop] to the right
        for i in range(n - 1, drop, -1):
            if nums[i] > nums[drop]:
                nums[i], nums[drop] = nums[drop], nums[i]
                break
        
        # Step 3: Reverse the subarray after drop
        nums[drop + 1:] = reversed(nums[drop + 1:])
