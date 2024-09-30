import collections

class OriginalSolution:
    def pacificAtlantic(self, heights):
        self.pacificCells = set()
        self.atlanticCells = set()
        self.rows = len(heights)
        self.cols = len(heights[0])



        for i in range(self.rows):
            for j in range(self.cols):
                self.dfs(heights, i, j, [])

        
        return list(self.pacificCells.intersection(self.atlanticCells))

    def dfs(self, heights, i, j, pathOfCells):
        neighbours = [[1,0], [0,1], [-1,0], [0,-1]]
        # check if we can go to any neighbouring cells
        queue = collections.deque([(i,j, [])])
        seen = set()
        while len(queue) > 0:
            (i,j, path) = queue.popleft()
            path = path + [[i,j]]
            seen.add((i,j))
                
            for k,l in neighbours:
                if (i + k >= 0 and (i+k) < self.rows and (j+l) >= 0 and (j+l) < self.cols and heights[i+k][j+l] <= heights[i][j] and (i+k, j+l) not in seen):
                    queue.append((i+k, j+l, path))
                
            if i == 0 or j == 0:
                for (a,b) in path:
                    self.pacificCells.add((a,b))
                


            if i == self.rows - 1 or j == self.cols - 1:
                for (a,b) in path:
                    self.atlanticCells.add((a,b))


class BetterSolution:
    def pacificAtlantic(self, heights):
        pacificCells = set()
        atlanticCells = set()
        self.rows = len(heights)
        self.cols = len(heights[0])
        self.heights = heights

        for i in range(self.rows):
            self.dfs(i, 0, pacificCells, 0)
            self.dfs(i, self.cols - 1, atlanticCells, 0)
        
        for j in range(self.cols):
            self.dfs(0, j, pacificCells, 0)
            self.dfs(self.rows - 1, j, atlanticCells, 0)
        
        return pacificCells.intersection(atlanticCells)

    
    def dfs(self, i, j, seen, prevHeight):
        if i >= 0 and i < self.rows and j >= 0 and j < self.cols and (i,j) not in seen and self.heights[i][j] >= prevHeight:
            seen.add((i,j))
            self.dfs(i + 1, j, seen, self.heights[i][j])
            self.dfs(i - 1, j, seen, self.heights[i][j])
            self.dfs(i, j + 1, seen, self.heights[i][j])
            self.dfs(i, j - 1, seen, self.heights[i][j])

heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
sln = BetterSolution()
print(sln.pacificAtlantic(heights))