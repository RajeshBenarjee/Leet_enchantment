import numpy as np
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        arr = np.array(matrix).flatten()
        arr.sort()
        low=0
        high=len(arr)-1
        while low<=high:
            mid=low+(high-low)//2
            if arr[mid]==target:
                return True
            elif arr[mid]>target:
                high=mid-1
            else:
                low=mid+1
        return False