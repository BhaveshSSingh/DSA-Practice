class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        # making the graph
        graph = collections.defaultdict(dict)
        for (x,y),val in zip(equations,values):
            graph[x][y] =val
            graph[y][x] = 1.0/val
        print(graph)
            
        # dfs function
        def dfs(x,y,visited):
            if x not in graph or y not in graph:
                return -1
            if y in graph[x]:
                return graph[x][y]
            
            for i in graph[x]:
                if i not in visited:
                    visited.add(i)
                    temp = dfs(i,y,visited)
                    if temp == -1:
                        continue
                    else:
                        return graph[x][i]*temp
            
            return -1
        
        res=[]
        for query in queries:
            res.append(dfs(query[0],query[1],set()))
        return res    
            