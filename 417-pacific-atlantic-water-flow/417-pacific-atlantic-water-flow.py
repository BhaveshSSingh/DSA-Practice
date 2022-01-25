class Solution(object):
    def pacificAtlantic(self, heights):
        ROWS, COLS = len(heights), len(heights[0])
        pac,atl = set(),set()
        
        def dfs(r,c,visit,prevHeight):
            if((r,c) in visit or r<0 or c<0 or r== ROWS  or c== COLS or heights[r][c] < prevHeight):
                return
            visit.add((r,c))
            dfs(r+1,c,visit,heights[r][c])
            dfs(r-1,c,visit,heights[r][c])
            dfs(r,c+1,visit,heights[r][c])
            dfs(r,c-1,visit,heights[r][c])
            
        # DFS throught the first row and the last row
        for c in range (COLS):
            # first row
            dfs(0,c,pac,heights[0][c])
            # last row
            dfs(ROWS -1,c,atl,heights[ROWS-1][c])
            
        # DFS through first col and last col
        for r in range (ROWS):
            # first col
            dfs(r,0,pac,heights[r][0])
            # last col
            dfs(r,COLS-1,atl,heights[r][COLS-1])
        
        res=[]
        for r in range (ROWS):
            for c in range( COLS):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])
        return res