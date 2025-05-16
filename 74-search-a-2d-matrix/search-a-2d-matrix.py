class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n=len(matrix)
        m=len(matrix[0])
        def binary(low,high):
            while low<=high:
                col=len(matrix[0])
                mid=(low+high)//2
                # print(mid)
                j=mid%col
                i=mid//col
                # print(i,j)
                # print(matrix[i][j])
                if matrix[i][j]==target:
                    return True 
                if matrix[i][j]<=target:
                    low=mid+1
                else:
                    high=mid-1
            return False
        return binary(0,(n*m)-1)

