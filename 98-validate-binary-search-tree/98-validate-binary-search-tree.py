def check(root,l,r):
    if root:
        return l<=root.val<=r and check(root.left,l,root.val-1) and check(root.right,root.val+1,r)
    return True 
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        inf=(2<<31)+1
        return check(root,-inf,inf)