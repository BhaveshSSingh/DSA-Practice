class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS,COLS = len(board),len(board[0])
        # 1 DFS
        def capture(r,c):      
            # this is the base case so if it isnt out of bound and it isnt too big and it isnt "O"
            # we can execute the below code of turing O to T
            if(r<0 or c<0 or r==ROWS or c==COLS or board[r][c] != "O"):
                return 
            board[r][c]="T"
            capture(r+1,c)
            capture(r-1,c)
            capture(r,c+1)
            capture(r,c-1)
            
        # 2 DFS capture unsurrounded region(0->T)
        for r in range(ROWS):
            for c in range(COLS):
                if (board[r][c] == "O" and 
                    (r in [0,ROWS-1] or c in [0,COLS-1])):
                    capture(r,c)
        
        # 3 Capture surrounded region (0-> X)
        for r in range(ROWS):
            for c in range (COLS):
                if board[r][c] == "O":
                    board[r][c] ="X"
                    
        #4 Uncapture surrounded region (t->O)
        for r in range(ROWS):
            for c in range (COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"
