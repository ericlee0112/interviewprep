import collections
'''
You are given a m x n 2D grid initialized with these three possible values:

-1 - A water cell that can not be traversed.
0 - A treasure chest.
INF - A land cell that can be traversed. We use the integer 2^31 - 1 = 2147483647 to represent INF.
Fill each land cell with the distance to its nearest treasure chest. If a land cell cannot reach a treasure chest than the value should remain INF.

Assume the grid can only be traversed up, down, left, or right.

Example 1:

Input: [
  [2147483647,-1,0,2147483647],
  [2147483647,2147483647,2147483647,-1],
  [2147483647,-1,2147483647,-1],
  [0,-1,2147483647,2147483647]
]

Output: [
  [3,-1,0,1],
  [2,2,1,-1],
  [1,-1,2,-1],
  [0,-1,3,4]
]

'''

class Solution:
    def islandsAndTreasure(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        queue = collections.deque([])
        neighbours = [0,1,0,-1,0]

        output = [[-1 for _ in range(cols)] for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    output[i][j] = 0
                    # add neighbours to queue
                    for k in range(len(neighbours) - 1):
                        newI = i + neighbours[k]
                        newJ = j + neighbours[k + 1]
                        if newI >= 0 and newI < rows and newJ >= 0 and newJ < cols and grid[newI][newJ] == 2147483647:
                            queue.append((1, newI, newJ))

        seen = set()

        while len(queue) > 0:
            distance, i, j = queue.popleft()
            seen.add((i,j))
            output[i][j] = distance

            for k in range(len(neighbours) - 1):
                newI = i + neighbours[k]
                newJ = j + neighbours[k + 1]
                if newI >= 0 and newI < rows and newJ >= 0 and newJ < cols and grid[newI][newJ] == 2147483647 and (newI, newJ) not in seen:
                    seen.add((newI, newJ))
                    queue.append((distance + 1, newI, newJ))
        
        for i in range(rows):
            for j in range(cols):
                grid[i][j] = output[i][j]

grid = [
  [2147483647,-1,0,2147483647],
  [2147483647,2147483647,2147483647,-1],
  [2147483647,-1,2147483647,-1],
  [0,-1,2147483647,2147483647]
]
sln = Solution()
print(sln.islandsAndTreasure(grid))




