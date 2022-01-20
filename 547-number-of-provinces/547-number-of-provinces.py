class Solution(object):
    def findCircleNum(self, isConnected):
        v = len(isConnected)
        parent = [i for i in range(v)]
        count = v
        for i in range(v):
            for j in range(i+1,v):
                if isConnected[i][j]==1:
                    pari,parj = i,j
                    while parent[pari] != pari:
                        pari = parent[pari]
                    while parent[parj] != parj:
                        parj = parent[parj]
                    if pari != parj:
                        count -=1
                        parent[pari] = parj
        return count