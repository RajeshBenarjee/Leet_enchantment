from typing import List

class Solution:
    def heapify(self, arr, n, i):
        smallest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[left] < arr[smallest]:
            smallest = left
        if right < n and arr[right] < arr[smallest]:
            smallest = right

        if smallest != i:
            arr[i], arr[smallest] = arr[smallest], arr[i]
            self.heapify(arr, n, smallest)

    def buildheap(self, arr, n):
        for i in range((n // 2) - 1, -1, -1):
            self.heapify(arr, n, i)

    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k]
        self.buildheap(heap, k)

        for i in range(k, len(nums)):
            if nums[i] > heap[0]:
                heap[0] = nums[i]
                self.heapify(heap, k, 0)

        return heap[0]
