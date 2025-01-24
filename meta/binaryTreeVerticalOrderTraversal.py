import collections
import heapq 

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def solution(self, root):
        self.hashmap = collections.defaultdict(list)
        self.traverse(root, 0)
        
        minheap = []
        for index in self.hashmap.keys():
            heapq.heappush(minheap, index)
        
        res = []
        while len(minheap) > 0:
            index = heapq.heappop(minheap)
            values = self.hashmap[index]
            res.append(values)
        
        return res

    
    def traverse(self, node, index):
        if node is not None:
            self.hashmap[index].append(node.val)
            self.traverse(node.left, index - 1)
            self.traverse(node.right, index + 1)



node = TreeNode(3)
node.left = TreeNode(9)
node.right = TreeNode(8)
node.left.left = TreeNode(4)
node.left.right = TreeNode(0)
node.right.left = TreeNode(1)
node.right.right = TreeNode(7)

sln = Solution()
print(sln.solution(node))
