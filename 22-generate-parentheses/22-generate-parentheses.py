class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        
        1. Only add open paranthasis if open < n
        2. Only add close paranthasis if close < open
        3. Valid if open == close == n 
        """
        stack = []
        res= []
        
        def backtrack(open,closed):
            if open == closed == n:
                return res.append("".join(stack))
            
            if open < n:
                stack.append("(")
                backtrack(open + 1,closed)
                stack.pop()
            
            if closed < open : 
                stack.append(")")
                backtrack(open,closed +1)
                stack.pop()
            
        backtrack(0,0)
        return res
            