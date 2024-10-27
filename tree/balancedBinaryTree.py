'''
Given a binary tree, return true if it is height-balanced and false otherwise.

A height-balanced binary tree is defined as a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

'''
class Solution:
    def isBalanced(self, root):
        res = self.traverse(root)
        return res[0]
        
        
    def traverse(self, node):
        if node is None:
            return (True, 0)
        
        leftBalanced, leftLength = self.traverse(node.left)
        rightBalanced, rightLength = self.traverse(node.right)

        totalLength = 1 + max(leftLength,rightLength)

        if leftBalanced and rightBalanced and abs(leftLength - rightLength) <= 1:
            return (True, totalLength)
        else:
            return (False, totalLength)

