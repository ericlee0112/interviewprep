# same tree https://leetcode.com/problems/same-tree/
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None and q is not None:
            return False
        elif p is not None and q is None:
            return False
        elif p is not None and q is not None and p.val == q.val:
            # compare
            return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        elif p is None and q is None:
            return True
        else:
            return False
            