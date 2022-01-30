def getSeq (root):
    if root:
        if not (root.right or root.left):
            return [root.val]
        return getSeq(root.right) + getSeq(root.left)
    return []
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        return getSeq(root1)== getSeq(root2)