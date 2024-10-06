# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
Given the root of a binary tree, determine if it is a complete binary tree.

In a complete binary tree, every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. 
It can have between 1 and 2h nodes inclusive at the last level h.

Example 1:

Input: root = [1,2,3,4,5,6]
Output: true
Explanation: Every level before the last is full (ie. levels with node-values {1} and {2, 3}), and all nodes in the last level ({4, 5, 6}) are as far left as possible.

Example 2:

Input: root = [1,2,3,4,5,null,7]
Output: false
Explanation: The node with value 7 isn't as far left as possible.
'''
import collections

class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        queue = collections.deque([(root, 0)])
        hashmap = collections.defaultdict(list)

        while len(queue) > 0:
            node, lvl = queue.popleft()
            if node is None:
                hashmap[lvl].append(None)
            else:
                hashmap[lvl].append(node.val)
                queue.append((node.left, lvl + 1))
                queue.append((node.right, lvl + 1))
        
        del(hashmap[lvl])

        incompleteLevel = False
        
        for lvl, nodes in hashmap.items():
            for i in range(len(nodes)):
                node = nodes[i]
                if i < len(nodes) - 1 and node is None:
                    incompleteLevel = True
                elif node is not None and incompleteLevel:
                    return False
                elif node is None:
                    incompleteLevel = True
        return True