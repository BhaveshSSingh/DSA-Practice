# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.sum_ = 0
        
        def ino(root):
            if root:
                if root.val > low:
                    ino(root.left)
                if low<= root.val <= high:
                    self.sum_ += root.val 
                if  root.val < high:
                    ino(root.right)
        ino(root)
        return self.sum_