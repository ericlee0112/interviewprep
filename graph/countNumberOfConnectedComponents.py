import collections
class Solution:
    def countComponents(self, n, edges):
        if len(edges) == 0:
            return n
        self.adjacencymap = collections.defaultdict(list)
        for (a,b) in edges:
            self.adjacencymap[a].append(b)
            self.adjacencymap[b].append(a)
        
        ans = 0
        for i in range(n):
            if len(self.adjacencymap[i]) > 0:
                ans += 1
                self.dfs(i)
        
        return ans
    
    def dfs(self, i):
        neighbours = self.adjacencymap[i]
        self.adjacencymap[i] = []
        for n in neighbours:
            self.dfs(n)
        
