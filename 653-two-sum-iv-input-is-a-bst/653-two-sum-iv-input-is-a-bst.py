def ino(l,root,k):
    if root:
        if k - root.val in l:
            return True
        l.add(root.val)
        return ino(l,root.left,k) or ino(l,root.right,k) 
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        nums = set()
        return ino(nums,root,k)