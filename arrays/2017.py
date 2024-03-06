# grid game
# https://leetcode.com/problems/grid-game/
'''
You are given a 0-indexed 2D array grid of size 2 x n, where grid[r][c] represents the number of points at position (r, c) on the matrix. Two robots are playing a game on this matrix.

Both robots initially start at (0, 0) and want to reach (1, n-1). Each robot may only move to the right ((r, c) to (r, c + 1)) or down ((r, c) to (r + 1, c)).

At the start of the game, the first robot moves from (0, 0) to (1, n-1), collecting all the points from the cells on its path. For all cells (r, c) traversed on the path, grid[r][c] is set to 0. Then, the second robot moves from (0, 0) to (1, n-1), collecting the points on its path. Note that their paths may intersect with one another.

The first robot wants to minimize the number of points collected by the second robot. In contrast, the second robot wants to maximize the number of points it collects. If both robots play optimally, return the number of points collected by the second robot.

Input: grid = [[2,5,4],
               [1,5,1]]
Output: 4
Explanation: The optimal path taken by the first robot is shown in red, and the optimal path taken by the second robot is shown in blue.
The cells visited by the first robot are set to 0.
The second robot will collect 0 + 0 + 4 + 0 = 4 points.

'''
class Solution:
    def gridGame(self, grid):
        if len(grid[0]) < 2:
            return 0
        # minmax
        toprow = [0 for i in range(len(grid[0]))]
        bottomrow = [0 for i in range(len(grid[1]))]
        
        for i in range(len(toprow) - 1, -1, -1):
            if i == len(grid[0]) - 1:
                toprow[i] = grid[0][i]
            else:
                toprow[i] = grid[0][i] + toprow[i + 1]
        
        for i in range(len(bottomrow)):
            if i == 0:
                bottomrow[i] = grid[1][i]
            else:
                bottomrow[i] = grid[1][i] + bottomrow[i - 1]


        min_val = float('inf')
        for i in range(len(grid[0])):
            if i == 0:
                min_val = min([min_val, toprow[i + 1]])
            elif i == len(grid[0]) - 1:
                min_val = min([min_val, bottomrow[i - 1]])
            else:
                min_val = min(min_val, max(toprow[i + 1], bottomrow[i - 1]))
        return min_val




grid = [[20,3,20,17,2,12,15,17,4,15],
        [20,10,13,14,15,5,2,3,14,3]]
sln = Solution()
print(sln.gridGame(grid))

'''
[[20, 23, 43, 60, 62, 74, 89, 106, 110, 125], 
 [40, 50, 63, 77, 92, 97, 99, 109, 124, 128]]

 [[0,3,20,17,2,12,15,17,4,15],
  [0,0,0,0,0,0,0,0,0,0]]

'''