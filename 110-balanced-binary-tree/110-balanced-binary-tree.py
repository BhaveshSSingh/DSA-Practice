def fn(root):
    if root:
        LHT = fn(root.left)
        RHT = fn(root.right)
        return 1+max(LHT,RHT) if LHT != None and RHT != None and abs(LHT - RHT ) < 2 else None
    return 0
    
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return fn(root) is not None 