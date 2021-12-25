class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        
        This is the intiuative approach sir was talking about with complex code
        """
        l,r = 0 , len(matrix) -1 
        
        while l < r:
            
            for i in range(r - l):
                top , bottom = l,r
                
                # save the top left(cleaner way of assigning without a lot of temp var)
                topLeft = matrix[top][l +i]
                
                matrix[top][l +i] = matrix[bottom -i][l]
                
                matrix[bottom - i][l] = matrix[bottom ][r - i]
                
                matrix[bottom ][r- i] = matrix[top + i][r]
                
                matrix[top + i][r] = topLeft
             
            # inner matrix
            r -=1
            l+=1


                
                
        