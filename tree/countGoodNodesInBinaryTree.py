# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0
        
        self.count = 0
        self.traverse(-float('inf'), root)
        return self.count
    
    def traverse(self, largestValSoFar, node):
        if node is None:
            return 
        if node.val >= largestValSoFar:
            self.count += 1
            self.traverse(node.val, node.left)
            self.traverse(node.val, node.right)
        else:
            self.traverse(largestValSoFar, node.left)
            self.traverse(largestValSoFar, node.right)