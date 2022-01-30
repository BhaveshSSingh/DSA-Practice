# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        if root:
            return str(root.val) + "(" +  self.serialize( root.left) + ")(" + self.serialize(root.right) + ")"
        return "X"
        

    def deserialize(self, data):
        if data == "X":
            return None
        data = data.split ( "(",1)
        n = TreeNode(int(data[0]))
        count = 1
        data = data[1]
        for i in range(len(data)):
            c =data[i]
            if c == "(":
                count +=1
            elif c == ")":
                count -=1
                if count == 0:
                    n.left, n.right = self.deserialize(data[:i]),self.deserialize(data[i+2:-1])
                    return n
                    

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))