# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
Given the root of a binary tree and an integer limit, delete all insufficient nodes in the tree simultaneously, and return the root of the resulting binary tree.

A node is insufficient if every root to leaf path intersecting this node has a sum strictly less than limit.

A leaf is a node with no children.
'''
class Solution:
    def sufficientSubset(self, root, limit):
        self.limit = limit
        res = self.traverse(root, 0 )
        if res == False:
            return None
        return root
    
    def traverse(self, node, pathSum):
        if node is None:
            return False
        
        if node.left is None and node.right is None:
            return (pathSum + node.val) >= self.limit
        
        leftResult = self.traverse(node.left, pathSum + node.val)
        if leftResult == False:
            node.left = None
        
        rightResult = self.traverse(node.right, pathSum + node.val)
        if rightResult == False:
            node.right = None
        
        if rightResult == False and leftResult == False:
            node = None
            return False
        