import collections

class Solution:
    def updateMatrix(self, mat):
        rows = len(mat)
        cols = len(mat[0])
        neighbours = [[1,0],[0,1],[-1,0],[0,-1]]

        queue = collections.deque([])

        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    queue.append((i,j))
                else:
                    mat[i][j] = -1
        
        while len(queue) > 0:
            i,j = queue.popleft()
            
            for (a,b) in neighbours:
                if (i + a) > -1 and (i+a) < rows and (j+b) > -1 and (j+b) < cols and mat[i + a][j + b] == -1:
                    mat[i + a][j + b] = mat[i][j] + 1
                    queue.append((i+a,j+b))
        return mat


'''
Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.
Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]

'''