from collections import defaultdict
import collections
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def countPairs(self, root, distance):
        self.pairs = 0
        self.distance = distance
        self.dfs(root)

        return self.pairs

    
    def dfs(self, node):
        if node is None:
            return []
        if node.left is None and node.right is None:
            return [1]
    
        leftDistances = self.dfs(node.left)
        rightDistances = self.dfs(node.right)

        for d1 in leftDistances:
            for d2 in rightDistances:
                if d1 + d2 <= self.distance:
                    self.pairs += 1


        totalDistances = leftDistances + rightDistances
        
        distancesToReturnToParent = []
        for distance in totalDistances:
            distancesToReturnToParent.append(distance + 1)
        
        return distancesToReturnToParent


class GraphSolution:
    def countPairs(self, root, distance):
        self.adjacencyMap = defaultdict(list)
        self.leafSet = set()
        self.distance = distance
        self.buildGraph(root)
        self.pairs = 0
        for node in self.leafSet:
            self.bfs(node)
        
        return self.pairs // 2

    
    def bfs(self, leafNode):
        visited = set([leafNode])
        queue = collections.deque([(leafNode, 0)])

        while len(queue) > 0:
            node, distanceFromLeaf = queue.popleft()

            if node != leafNode and node in self.leafSet and distanceFromLeaf <= self.distance:
                self.pairs += 1
            
            for neighbouringNode in self.adjacencyMap[node]:
                if neighbouringNode not in visited:
                    queue.append((neighbouringNode, distanceFromLeaf + 1))
                    visited.add(neighbouringNode)

    
    def buildGraph(self, node):
        if node is None:
            return
        if node.left is not None:
            self.adjacencyMap[node].append(node.left)
            self.adjacencyMap[node.left].append(node)
        if node.right is not None:
            self.adjacencyMap[node].append(node.right)
            self.adjacencyMap[node.right].append(node)
        if node.left is None and node.right is None:
            self.leafSet.add(node)
        
        self.buildGraph(node.left)
        self.buildGraph(node.right)

                                