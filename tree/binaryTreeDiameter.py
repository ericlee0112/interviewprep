


class Solution:
    def diameterOfBinaryTree(self, root):
        self.maxDiameter = 0

        self.traverse(root)

        return self.maxDiameter
    
    def traverse(self, node):
        if node is None:
            return 0
        left = self.traverse(node.left)
        right = self.traverse(node.right)

        self.maxDiameter = (self.maxDiameter, left + right)
        return 1 + max(left, right)
    