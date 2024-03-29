# subtree of another tree https://leetcode.com/problems/subtree-of-another-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # perform bfs 
        if root is None:
            return False

        queue = collections.deque([(root)])

        while len(queue) > 0:
            node = queue.popleft()
            if node.val == subRoot.val:
                res = self.sameTree(node, subRoot)
                if res:
                    return True
            if node.left is not None:
                queue.append((node.left))
            if node.right is not None:
                queue.append((node.right))
        
        return False
    
    def sameTree(self, tree1, tree2):
        if tree1 is not None and tree2 is None:
            return False
        elif tree1 is None and tree2 is not None:
            return False
        elif tree1 is not None and tree2 is not None and tree1.val == tree2.val:
            return self.sameTree(tree1.left, tree2.left) and self.sameTree(tree1.right, tree2.right)
        elif tree1 is None and tree2 is None:
            return True
        else:
            return False