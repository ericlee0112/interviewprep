# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
for a BST, left subtree contains values less than root
right subtree contains values greater than root
'''

class Solution:
    def isValidBST(self, root):
        return self.isValidNode(-float('inf'), float('inf'), root)
    
    def isValidNode(self, lowerBound, upperBound, node):
        if node is None:
            return True
        if node.val > lowerBound and node.val < upperBound:
            return self.isValidNode(lowerBound, node.val, node.left) and self.isValidNode(node.val, upperBound, node.right)
        else:
            return False