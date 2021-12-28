class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        NeetCode Solution
        """
        row,cols = len(matrix), len(matrix[0])
        rowZero = False
        # Determine which row and col need to be zero
        for r in range(row):
            for c in range(cols):
                if matrix[r][c] == 0:
                    matrix [0][c] = 0
                    # because rowZero is set to false
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        rowZero = True
        # zero in the main part of the matrix
        for r in range(1,row):
            for c in range(1,cols):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
        
        # zeroing the first COl if we need to 
        if matrix[0][0] == 0:
            for r in range(row):
                matrix[r][0]=0
        
        # zeroing  the first row if we need to
        if rowZero:
            for c in range(cols):
                if matrix[0][c] == 0:
                    for r in range(1, row):
                        matrix[r][c] = 0
                else:
                    matrix[0][c] = 0
            
