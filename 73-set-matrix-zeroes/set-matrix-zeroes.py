class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # For normal traversal it would take O(N^2) 
        # bu using the flatten method row%no of colums it could take O(n*m)
        m = len(matrix)        # Number of rows
        n = len(matrix[0])     # Number of columns
        zero_positions = []

        # Step 1: Identify all zero positions (flattened traversal)
        for index in range(m * n):
            row = index // n
            col = index % n
            if matrix[row][col] == 0:
                zero_positions.append((row, col))

        # Step 2: Set corresponding rows and columns to 0
        for row, col in zero_positions:
            for j in range(n):
                matrix[row][j] = 0
            for i in range(m):
                matrix[i][col] = 0
