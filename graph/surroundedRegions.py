import collections
class Solution:
    def solve(self, board):
        if len(board) < 3 or len(board[0]) < 3:
            return

        self.rows = len(board)
        self.cols = len(board[0])
        

        # check only inner cells
        for i in range(1,self.rows - 1):
            for j in range(1, self.cols - 1):
                if board[i][j] == "O":
                    # check if cell can be surrounded
                    res = self.isSurrounded(board, i, j)
                    if res:
                        self.infect(board, i, j)
        
        
    def infect(self, board, i, j):
        neighbours = [0,1,0,-1,0]
        if i > 0 and i < self.rows and j > 0 and j < self.cols and board[i][j] == "O":
            board[i][j] = "X"
            for k in range(len(neighbours) - 1):
                newI = i + neighbours[k]
                newJ = j + neighbours[k + 1]
                self.infect(board, newI, newJ)
    
    def isSurrounded(self, board, row, col):
        seen = set()
        seen.add((row, col))
        neighbours = [0,1,0,-1,0]

        queue = collections.deque([(row, col)])

        while len(queue) > 0:
            i, j = queue.popleft()

            if i == 0 or i == (self.rows - 1) or j == 0 or j == (self.cols - 1):
                return False
            if i > 0 and i < self.rows - 1 and j > 0 and j < self.cols - 1 and board[i][j] == "O":
                for k in range(len(neighbours) - 1):
                    newI = i + neighbours[k]
                    newJ = j + neighbours[k + 1]
                    if newI >= 0 and newI <= self.rows - 1 and newJ >= 0 and newJ <= self.cols - 1 and board[newI][newJ] == "O" and (newI, newJ) not in seen:
                        queue.append((newI, newJ))
                        seen.add((newI, newJ))
        return True






board = [["O","X","X","O","X"],
         ["X","O","O","X","O"],
         ["X","O","X","O","X"],
         ["O","X","O","O","O"],
         ["X","X","O","X","O"]]
'''
output = [["O","X","X","O","X"],
          ["X","X","X","X","O"],
          ["X","X","X","X","X"],
          ["O","X","X","X","X"],
          ["X","X","X","X","X"]]

expected = [["O","X","X","O","X"],
            ["X","X","X","X","O"],
            ["X","X","X","O","X"],
            ["O","X","O","O","O"],
            ["X","X","O","X","O"]]


'''

sln = Solution()
print(sln.solve(board))






