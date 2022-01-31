def f(root,sm):
    if root:
        sm = f(root.right, sm)
        root.val += sm
        return f(root.left,root.val)
    return sm
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        f(root,0)
        return root