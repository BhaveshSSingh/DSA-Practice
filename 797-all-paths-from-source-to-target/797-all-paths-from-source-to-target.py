def f(src,graph):
    if src == len(graph)-1:
        return [[len(graph)-1]]
    ans =[]
    for adjNode in graph[src]:
        ans.extend([[src]+x for x in f(adjNode,graph)])
    return ans

class Solution(object):
    def allPathsSourceTarget(self, graph):
        return f(0,graph)
        