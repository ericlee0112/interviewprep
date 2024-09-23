'''
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

You are given two integer arrays preorder and inorder.

    preorder is the preorder traversal of a binary tree
    inorder is the inorder traversal of the same tree
    Both arrays are of the same size and consist of unique values.

Rebuild the binary tree from the preorder and inorder traversals and return its root.

Input: preorder = [1,2,3,4], inorder = [2,1,3,4]

Output: [1,2,3,null,null,null,4]


  1
 / \
2   3
     \
      4   
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder, inorder):
        if len(preorder) == 0 or len(inorder) == 0:
            return None
        
        root = TreeNode(preorder[0])
        middle_index = inorder.index(preorder[0])

        root.left = self.buildTree(preorder[1:middle_index + 1], inorder[:middle_index])
        root.right = self.buildTree(preorder[middle_index + 1:], inorder[middle_index + 1:])
        return root

