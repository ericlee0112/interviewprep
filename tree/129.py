# sum root to leaf numbers
# https://leetcode.com/problems/sum-root-to-leaf-numbers/description/
'''
You are given the root of a binary tree containing digits from 0 to 9 only.

Each root-to-leaf path in the tree represents a number.

For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.

A leaf node is a node with no children.

'''
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


import collections
class Solution:
    def sumNumbers(self, root):
        self.paths = []
        # traverse through tree
        if root is None:
            return 0
        elif root.left is None and root.right is None:
            return root.val
        
        if root.left is not None:
            self.traverse(root.left, str(root.val))
        if root.right is not None:
            self.traverse(root.right, str(root.val))
        
        return sum(self.paths)
    
    def traverse(self, node, prefixValue):
        if node is not None:
            nodeValue = node.val
            if node.left is None and node.right is None:
                self.paths.append(int(prefixValue + str(nodeValue)))
            if node.left is not None:
                self.traverse(node.left, prefixValue + str(nodeValue))
            if node.right is not None:
                self.traverse(node.right, prefixValue + str(nodeValue))


sln = Solution()
print(sln.sumNumbers(node))
