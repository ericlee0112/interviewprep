# https://leetcode.com/problems/binary-tree-right-side-view/
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

node = TreeNode(1)
node.left = TreeNode(2)
node.left.right = TreeNode(5)
node.right = TreeNode(3)
node.right.right = TreeNode(4)


import collections
class Solution:
    def rightSideView(self, root: TreeNode):
        if root is None:
            return []
        
        res = []
        hashset = set()
        queue = collections.deque([(root, 0)])
        while len(queue) > 0:
            node, lvl = queue.popleft()
            if lvl not in hashset:
                res.append(node.val)
                hashset.add(lvl)
            # add right then left
            if node.right is not None:
                queue.append((node.right, lvl + 1))
            if node.left is not None:
                queue.append((node.left, lvl + 1))
        return res

        
sln = Solution()
print(sln.rightSideView(node))