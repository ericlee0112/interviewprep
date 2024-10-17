class Solution:
    def wordSearch(self, board, word):
        self.rows = len(board)
        self.cols = len(board[0])
        self.board = board
        self.word = word

        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j] == word[0]:
                    res = self.dfs(i,j,0)
                    if res:
                        return True
        return False

    def dfs(self, i, j, index):
        if index == len(self.word):
            return True
      
        if i > -1 and i < self.rows and j > -1 and j < self.cols and self.board[i][j] == self.word[index]:
            char = self.board[i][j]
            self.board[i][j] = "*"
            # check neighbours
            res = self.dfs(i+1, j, index+1) or self.dfs(i, j+1, index+1) or self.dfs(i, j-1, index+1) or self.dfs(i-1, j, index+1) 
            self.board[i][j] = char
            if res:
                return True
            else:
                return False
        return False

