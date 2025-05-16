class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row=len(matrix)
        col=len(matrix[0])
        s_row=0
        s_col=0
        end_row=row-1
        end_col=col-1
        res=[]
        while(s_row<=end_row and s_col<=end_col):
            # left to right 
            for i in range(s_col,end_col+1):
                res.append(matrix[s_row][i])
            s_row+=1
            # top to bottom
            for i in range(s_row,end_row+1):
                res.append(matrix[i][end_col])
            end_col-=1
            # right to left
            if s_row<=end_row:
                for i in range(end_col,s_col-1,-1):
                    res.append(matrix[end_row][i])
                end_row-=1
            # bottom to up
            if s_col<=end_col:
                for i in range(end_row,s_row-1,-1):
                    res.append(matrix[i][s_col])
                s_col+=1
        return res

