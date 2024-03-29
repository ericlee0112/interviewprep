# https://leetcode.com/problems/island-perimeter/description/
'''
You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

Input: grid = 
[[0,1,0,0],
[1,1,1,0],
[0,1,0,0],
[1,1,0,0]]
Output: 16
Explanation: The perimeter is the 16 yellow stripes in the image above.
'''
class Solution:
    def islandPerimeter(self, grid):
        self.rows = len(grid) - 1
        self.cols = len(grid[0]) - 1
        # rules 
        # if corner (i == 0 and j == 0) (i == len(rows) - 1 and j == len(cols) - 1) (i == 0 and j == len(cols) - 1) (i == len(rows) - 1 and j == 0)
        # if edge (i == 0) (i == len(rows) - 1) (j == 0) (j == len(cols) - 1)
        perimeter = 0

        for i in range(self.rows + 1):
            for j in range(self.cols + 1):
                # check neighbours
                if grid[i][j] == 1:
                    p = self.checkNeighbours(grid, i, j)
                    perimeter += p
        return perimeter
                
    def checkNeighbours(self, grid, i, j):
        perimeter = 0
        neighbours = [[0,-1], [0,1], [-1,0], [1,0]]
        for (k,l) in neighbours:
            new_i = i + k
            new_j = j + l
            if new_i < 0:
                perimeter += 1
            elif new_j < 0:
                perimeter += 1
            elif new_i > self.rows:
                perimeter += 1
            elif new_j > self.cols:
                perimeter += 1
            # check if new_i and new_j are within bounds
            elif new_i >= 0 and new_i <= self.rows and new_j >= 0 and new_j <= self.cols and grid[new_i][new_j] == 0:
                perimeter += 1

        return perimeter

sln = Solution()
grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
print(sln.islandPerimeter(grid))

