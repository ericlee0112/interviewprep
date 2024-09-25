'''
Given a square n x n matrix of integers matrix, rotate it by 90 degrees clockwise.

You must rotate the matrix in-place. Do not allocate another 2D matrix and do the rotation.
'''
class Solution:
    def rotate(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])

        for j in range(cols):
            newRow = []
            for i in range(rows - 1, -1, -1):
                newRow.append(matrix[i][j])
            matrix.append(newRow)
        
        for i in range(rows):
            del(matrix[0])
        
        