'''
create a function that takes in 
- an integer that represents number of years
- a 2d matrix filled with 0s and 1s that describes a garden. 1s represent hedges, and 0s represent empty spaces 

rules
- an empty square that is adjacent to a hedge (including diagonally) will be filled in the next year
- a square surrounded by all 8 sides will be empty the next year

return the number of pairs of adjacent hedges 

e.g.
years = 1
matrix = [[0,0,1],
          [0,0,0]]

output =[[0,1,1]
         [0,1,1]] which means 6 total adjacent pairs
'''

class Solution:
    def growingHedges(self, n, matrix):
        # run simulation in a loop n times
        self.rows = len(matrix)
        self.cols = len(matrix[0])

        for i in range(n):
            newMatrix = self.simulation(matrix)
            print(newMatrix)
            matrix = newMatrix
        
        pairs = set()
        neighbours = [[0,1],[0,-1],[1,0],[1,1],[1,-1],[-1,1],[-1,0],[-1,-1]]

        # count pairs 
        totalPairs = 0
        for i in range(self.rows):
            for j in range(self.cols):
                # get pairs at (i,j)
                if matrix[i][j] == 1:
                    pairs = 0
                    for (a,b) in neighbours:
                        newI = i + a
                        newJ = j + b
                        if newI >= 0 and newI < self.rows and newJ >= 0 and newJ < self.cols and matrix[newI][newJ] == 1:
                            pairs += 1
                totalPairs += (pairs // 2)
        
        return totalPairs


    
    def simulation(self, matrix):
        neighbours = [[-1,-1], [-1,0], [-1,1], [0,-1], [0,1], [1,-1],[1,0],[1,1]]

        for i in range(self.rows):
            for j in range(self.cols):
                if matrix[i][j] == 1:
                    res = self.checkIfSurrounded(matrix, i, j)
                    if res:
                        matrix[i][j] = -1
        
        for i in range(self.rows):
            for j in range(self.cols):
                if matrix[i][j] == 1:
                    # mark surrounding cells to be grown next year
                    for (a,b) in neighbours:
                        newI = i + a
                        newJ = j + b
                        if newI >= 0 and newI < self.rows and newJ >= 0 and newJ < self.cols and matrix[newI][newJ] == 0:
                            matrix[newI][newJ] = 2
        
        # convert marked cells
        for i in range(self.rows):
            for j in range(self.cols):
                if matrix[i][j] == -1:
                    matrix[i][j] = 0
                elif matrix[i][j] == 2:
                    matrix[i][j] = 1
        
        return matrix
    
    def checkIfSurrounded(self, matrix, i, j):
        neighbours = [[-1,-1], [-1,0], [-1,1], [0,-1], [0,1], [1,-1],[1,0],[1,1]]
        for (a,b) in neighbours:
            newI = i + a
            newJ = j + b
            if newI >= 0 and newI < self.rows and newJ >= 0 and newJ < self.cols and matrix[newI][newJ] == 1:
                continue
            else:
                return False
        return True
    
sln = Solution()
matrix = [[1, 0, 0, 0],
          [1, 1, 0, 0],
          [1, 0, 0, 1]]
n = 6

print(sln.growingHedges(6, matrix))