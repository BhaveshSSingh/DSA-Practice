class Solution(object):
    def numIslands(self, grid):
        count = 0
        m,n = len(grid),len(grid[0])      
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    count += 1
                    s = set([(i,j)])
                    while s:
                        ei, ej = s.pop()
                        grid[ei][ej]="0"
                        if ei+1<m and grid[ei+1][ej] == "1":
                            s.add((ei+1,ej))
                            
                        if ei>0 and grid[ei-1][ej] == "1":
                            s.add((ei-1,ej))
                            
                        if ej+1<n and grid[ei][ej+1] == "1":
                            s.add((ei,ej+1))
                            
                        if ej>0 and grid[ei][ej-1] == "1":
                            s.add((ei,ej-1))
        return count
        