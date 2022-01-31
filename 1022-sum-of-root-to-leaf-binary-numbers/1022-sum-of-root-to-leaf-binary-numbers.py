def f(root,ans):
    if root:
        ans = (2*ans + root.val)
        if not(root.left or root.right):
            return ans
        return f(root.left,ans) + f(root.right,ans)
    return 0
            
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        return f(root,0)