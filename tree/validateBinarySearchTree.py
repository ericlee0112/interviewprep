class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

node = TreeNode(4)
node.left = TreeNode(9)
node.left.left = TreeNode(5)
node.left.right = TreeNode(1)
node.right = TreeNode(0)

'''
Given the root of a binary tree, return true if it is a valid binary search tree, otherwise return false.

A valid binary search tree satisfies the following constraints:

The left subtree of every node contains only nodes with keys less than the node's key.
The right subtree of every node contains only nodes with keys greater than the node's key.
Both the left and right subtrees are also binary search trees.
'''


class Solution:
    def isValidBST(self, root):
        return self.validate(float('-inf'), float('inf'), root)

    def validate(self, lowerbound, upperbound, node):
        if node is None:
            return True
        if lowerbound < node.val and node.val < upperbound:
            return self.validate(node.val, upperbound, node.left) and self.validate(lowerbound, node.val, node.right)
        else:
            return False
    
