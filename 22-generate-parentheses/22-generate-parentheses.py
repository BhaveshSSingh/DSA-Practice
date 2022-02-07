class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        stack =[]
        res=[]
        
        
        def backtrack(open,closed):
            if open == closed == n:
                res.append("".join(stack))
            
            if open > closed:
                stack.append(")")
                backtrack(open,closed+1)
                stack.pop()
            
            if open < n:
                stack.append("(")
                backtrack(open+1,closed)
                stack.pop()
        
        backtrack(0,0)
        return res
        