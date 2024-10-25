'''
You are given a network of n directed nodes, labeled from 1 to n. You are also given times, a list of directed edges where times[i] = (ui, vi, ti).

ui is the source node (an integer from 1 to n)
vi is the target node (an integer from 1 to n)
ti is the time it takes for a signal to travel from the source to the target node (an integer greater than or equal to 0).
You are also given an integer k, representing the node that we will send a signal from.

Return the minimum time it takes for all of the n nodes to receive the signal. If it is impossible for all the nodes to receive the signal, return -1 instead.


Input: times = [[1,2,1],[2,3,1],[1,4,4],[3,4,1]], n = 4, k = 1

Output: 3
'''

import collections
import heapq
class Solution:
    def networkDelayTime(self, times, numberOfNodes, k):
        directionMap = collections.defaultdict(list)
        for (source, target, time) in times:
            directionMap[source].append((time, target))

        minheap = [[0,k]]

        visited = set()

        totalTime = 0

        while len(visited) < numberOfNodes and len(minheap) > 0:
            time, node = heapq.heappop(minheap)
            print((time, node))
            if node in visited:
                continue
            totalTime = time
            visited.add(node)

            neighbouringNodes = directionMap[node]

            for (neighbourTime, neighbourNode) in neighbouringNodes:
                heapq.heappush(minheap, (time + neighbourTime, neighbourNode))

        if len(visited) < numberOfNodes:
            return -1
        else:   
            return totalTime