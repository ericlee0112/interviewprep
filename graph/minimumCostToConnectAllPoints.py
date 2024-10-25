# minimum spanning trees - prims algorithm
'''
prims algorithm

to connect n nodes (no cycles), it will require n - 1 edges

we also want to minimize total cost to connect the nodes

1. we can start at any node, perform bfs on that node 


the cost of connecting two points is the manhattan distance between them

return minimum cost to make all points connected


'''

import collections
import heapq

class Solution:
    def minCostConnectPoints(self, points):
        adjacencyMap = collections.defaultdict(list) # i -> list of [cost, node]
        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i + 1, len(points)):
                x2, y2 = points[j]
                distance = abs(x1 - x2) + abs(y1 - y2)
                adjacencyMap[i].append((distance, j))
                adjacencyMap[j].append((distance, i))
        
        # prims algorithm
        totalCostToConnectAllPoints = 0
        minheap = [[0,0]]
        visitedNodes = set()
        while len(visitedNodes) < len(points):
            (cost, node) = heapq.heappop(minheap)
            if node in visitedNodes:
                continue
            totalCostToConnectAllPoints += cost
            visitedNodes.add(node)
            for neighbouringCost, neighbouringNode in adjacencyMap[node].items():
                heapq.heappush(minheap, (neighbouringCost, neighbouringNode))
        
        return totalCostToConnectAllPoints
