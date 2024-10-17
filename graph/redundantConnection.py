import collections

class Solution:
    def findRedundantConnection(self, edges):
        self.n = len(edges)
        for i in range(len(edges) -1, -1, -1):
            
            res = self.checkGraph(edges[:i] + edges[i + 1:])
            if res:
                return edges[i]
        
        return []

    def checkGraph(self, edges):
        hashmap = collections.defaultdict(list)
        seen = set()

        for (a,b) in edges:
            hashmap[a].append(b)
            hashmap[b].append(a)

        queue = collections.deque([(1)])

        while len(queue) > 0:
            node = queue.popleft()
            seen.add(node)
            neighbours = hashmap[node]
            for n in neighbours:
                if n not in seen:
                    queue.append((n))
        
        return len(seen) == self.n
    
sln = Solution()
edges = [[1,2],[1,3],[3,4],[2,4]]

print(sln.findRedundantConnection(edges))