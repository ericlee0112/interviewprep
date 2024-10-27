'''
a path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has a edge connecting them. 
a node can only appear in a sequence at most once. 

the path does not need to pass through the root

find maximum path sum of any path


use depth first search, resulting in O(n)

'''

import collections

class Solution:
    def maxPathSum(self, root):
        self.res = root.val
        self.getMaxPathAtNode(root)
        return self.res
    
    # return max path sum without splitting
    def getMaxPathAtNode(self, node):
        if node is None:
            return 0
        leftPath = self.getMaxPathAtNode(node.left)
        rightPath = self.getMaxPathAtNode(node.right)
        leftPath = max(leftPath, 0)
        rightPath = max(rightPath, 0)

        # what if we chose to split at this node, update the res accordingly
        self.res = max(self.res, node.val + leftPath + rightPath)
        
        # return to parent node, assuming that the split occured above this node
        return node.val + max(leftPath, rightPath)
