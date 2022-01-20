class Solution(object):
    def findRedundantConnection(self, edges):
        parent = [i for i in range(1001)]
        for e in edges:
            pari,parj = e
            while parent[pari] != pari:
                pari = parent[pari]
            while parent[parj] != parj:
                parj= parent[parj]
            if pari !=parj:
                parent[pari]= parj
            else:
                return e