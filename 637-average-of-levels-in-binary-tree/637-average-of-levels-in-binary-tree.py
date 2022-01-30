# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        ans = []
        curr = []
        q  = deque([None, root])
        while True:
            node = q.pop()
            if not node:
                ans.append(sum(curr)/len(curr))
                if len(q)<1:
                    return ans
                    return 
                curr =[]        
                q.appendleft(None)
                continue
            curr.append(node.val)
            if node.left:
                q.appendleft(node.left)
            if node.right:
                q.appendleft(node.right)