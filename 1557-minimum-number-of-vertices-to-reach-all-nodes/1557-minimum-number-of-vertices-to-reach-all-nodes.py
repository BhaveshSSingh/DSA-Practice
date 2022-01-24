class Solution(object):
    def findSmallestSetOfVertices(self, n, edges):
        inD = [ 0 for i in range (n)]
        for t in edges:
            inD[t[1]] += 1
        ans =[]
        for i in range(n):
            if inD[i]== 0:
                ans.append(i)
        return ans
        