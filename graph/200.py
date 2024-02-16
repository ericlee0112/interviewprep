# number of islands
'''
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.


Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3


'''
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

def numberOfIslands(grid):
    num_of_rows = len(grid)
    num_of_cols = len(grid[0])
    islands = 0
    # nested for loop through grid
    for i in range(num_of_rows):
        for j in range(num_of_cols):
            # if cell is land, sink the island, and increment islands += 1
            if grid[i][j] == "1":
                islands += 1
                sink(grid, i, j)
    return islands

def sink(grid, i, j):
    neighbours = [[1,0], [0,1], [-1,0], [0,-1]]
    # sink the cell [i,j] and any connecting land cells 
    if i >= 0 and i < len(grid) and j >= 0 and j < len(grid[0]) and grid[i][j] == "1":
        grid[i][j] = "0"
        for k,l in neighbours:
            # check neighbouring cells
            sink(grid, i + k, j + l)


print(numberOfIslands(grid))