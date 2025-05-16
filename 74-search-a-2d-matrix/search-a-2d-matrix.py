import numpy as np
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if target in np.array(matrix).flatten():
            return True
        else:
            return False