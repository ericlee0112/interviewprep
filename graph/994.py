# rotting oranges
'''
You are given an m x n grid where each cell can have one of three values:

    0 representing an empty cell,
    1 representing a fresh orange, or
    2 representing a rotten orange.

Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

Input: grid = 
[[2,1,1],
 [1,1,0],
 [0,1,1]]
Output: 4
'''
class Solution:
    def orangesRotting(self, grid): 
        fresh_oranges = self.countFresh(grid)
        days = 0


        while fresh_oranges > 0:
            self.rows = len(grid)
            self.cols = len(grid[0])
            # keep track of days
            # keep track of remaining fresh oranges

            # mark the oranges to infect
            marked = 0
            neighbours = [[1,0], [0,1], [-1,0], [0,-1]]
            for i in range(self.rows):
                for j in range(self.cols):
                    if grid[i][j] == 2:
                        # mark the surrounding oranges
                        for k,l in neighbours:
                            if (i+k) >= 0 and (i+k) < self.rows and (j+l) >= 0 and (j+l) < self.cols and grid[i + k][j + l] == 1:
                                grid[i + k][j + l] = 3
                                marked += 1

            if marked == 0:
                if fresh_oranges == 0:
                    return days
                else:
                    return -1
                
            fresh_oranges -= marked

            # infect method
            self.infect(grid)

            print(grid)

            # increment day += 1
            days += 1
        return days
    
    def mark(self, grid):
        marked = 0
        neighbours = [[1,0], [0,1], [-1,0], [0,-1]]
        for i in range(self.rows):
            for j in range(self.cols):
                if grid[i][j] == 2:
                    # mark the surrounding oranges
                    for k,l in neighbours:
                        if grid[i + k][j + l] == 1:
                            grid[i + k][j + l] = 3
                            marked += 1
        return grid

    def infect(self, grid):
        for i in range(self.rows):
            for j in range(self.cols):
                if grid[i][j] == 3:
                    grid[i][j] = 2


    
    def countFresh(self, grid):
        fresh = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh += 1
        return fresh


grid = [[2,1,1],[0,1,1],[1,0,1]]

sln = Solution()
print(sln.orangesRotting(grid))