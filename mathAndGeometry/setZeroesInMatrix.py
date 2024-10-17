'''
Given an m x n matrix of integers matrix, if an element is 0, set its entire row and column to 0's.

You must update the matrix in-place.

Input: matrix = [
  [0,1],
  [1,1]
]

Output: [
  [0,0],
  [0,1]
]

Input: matrix = [
  [1,2,3],
  [4,0,5],
  [6,7,8]
]

Output: [
  [1,0,3],
  [0,0,0],
  [6,0,8]
]



'''

class Solution:
    def setZeroes(self, matrix):
        markedCols = set()
        markedRows = set()
        numOfRows = len(matrix)
        numOfCols = len(matrix[0])
        
        for i in range(numOfRows):
            for j in range(numOfCols):
                if matrix[i][j] == 0:
                    markedCols.add(j)
                    markedRows.add(i)
        
        for i in range(numOfRows):
            for j in range(numOfCols):
                if i in markedRows or j in markedCols:
                    matrix[i][j] = 0
        