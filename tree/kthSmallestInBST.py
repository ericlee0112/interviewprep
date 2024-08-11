'''
Given the root of a binary search tree, and an integer k,
return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# asuming that this is a BST
node = TreeNode(3)
node.left = TreeNode(1)
node.left.right = TreeNode(2)
node.right = TreeNode(4)

def kthSmallest(root, k):
    stack = []
    index = 0
    curr = root

    while stack is not None or curr is not None:
        while curr is not None:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        index += 1
        if index == k:
            return curr.val
        curr = curr.right
    return curr.val


res = kthSmallest(node, 2)
print(res)