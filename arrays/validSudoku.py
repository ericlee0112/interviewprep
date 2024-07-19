# valid sudoku
'''
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

    Each row must contain the digits 1-9 without repetition.
    Each column must contain the digits 1-9 without repetition.
    Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:

    A Sudoku board (partially filled) could be valid but is not necessarily solvable.
    Only the filled cells need to be validated according to the mentioned rules.

Example 1:
Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true

Example 2:
Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
'''

class Solution:
    def sudoku(self, grid):
        sectors = [0,3,6]
        # check every cell

        # validate three things
            # every row
            # every column
            # every sector [0-2] [3-5] [6-8]
        
        for i in range(9):
            row = grid[i]
            # valdate row 
            col = [grid[j][i] for j in range(9)]
            # validate col
            if self.validateList(row) == False or self.validateList(col) == False:
                return False
        
        for i in sectors:
            for j in sectors:
                if self.validateSector(grid, i, j) == False:
                    return False
        
        return True


    def validateSector(self, grid, i, j):
        # i,j is the north western most index of the sector
        hashset = set()
        for a in range(i, i+3):
            for b in range(j, j+3):
                element = grid[a][b]
                if element != '.':
                    if element not in hashset:
                        hashset.add(element)
                    else:
                        return False
        return True

        

    def validateList(self, array):
        hashset = set()
        for element in array:
            if element != '.':
                if element not in hashset:
                    hashset.add(element)
                else:
                    return False
        return True

grid =[[".",".","4",".",".",".","6","3","."],
       [".",".",".",".",".",".",".",".","."],
       ["5",".",".",".",".",".",".","9","."],
       [".",".",".","5","6",".",".",".","."],
       ["4",".","3",".",".",".",".",".","1"],
       [".",".",".","7",".",".",".",".","."],
       [".",".",".","5",".",".",".",".","."],
       [".",".",".",".",".",".",".",".","."],
       [".",".",".",".",".",".",".",".","."]]
sln = Solution()
print(sln.sudoku(grid))