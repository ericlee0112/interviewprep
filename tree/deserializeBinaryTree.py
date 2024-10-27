'''
implement an algorithm to serialize and deserialize a binary tree

'''
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class TreeSerializer:
    def serialize(self, node):
        self.data = []
        self.dfsSerialize(node)
        return self.data

    def dfsSerialize(self, node):
        if node is None:
            self.data.append("N")
            return
        
        self.data.append(str(node.val))
        self.dfsSerialize(node.left)
        self.dfsSerialize(node.right)

    
    def deSerialize(self, data):
        self.nodeValues = data.split(",")
        self.i = 0
        rootNode = self.dfsDeserialize()
        return rootNode

    def dfsDeserialize(self):
        if self.nodeValues[self.i] == "N":
            self.i += 1
            return None
        node = TreeNode(int(self.nodeValues[self.i]))
        node.left = self.dfsDeserialize()
        node.right = self.dfsDeserialize()
        return node