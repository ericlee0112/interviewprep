import collections

class Node:
    def __init__(self, val, neighbours):
        self.val = val
        self.neighbours = neighbours

class Solution:
    def cloneGraph(self, node):
        self.oldToNew = collections.defaultdict(Node)
        return self.dfs(node)

    
    def dfs(self, node):
        if node in self.oldToNew:
            return self.oldToNew[node]

        copyNode = Node(node.val)
        self.oldToNew[node] = copyNode

        for neighbor in node.neighbors:
            copyNeighbor = self.dfs(neighbor)
            self.oldToNew(copyNeighbor)

        return copyNode