'''
n x n integer matrix board laelled from 1 to n2

you start at square 1. in each move, starting from square curr, you do the following:
    - choose destination square next with a label in the range (curr +1, min(curr + 6, n2))
    - if next square has snake or ladder, you move to that destination. otherwise, you move to next
    - game ends when you reach n2

return the least number of moves required to reach square n2. if it is not possible, return -1

board = [[-1,-1,-1,-1,-1,-1],
         [-1,-1,-1,-1,-1,-1],
         [-1,-1,-1,-1,-1,-1],
         [-1,35,-1,-1,13,-1],
         [-1,-1,-1,-1,-1,-1],
         [-1,15,-1,-1,-1,-1]]


''' 
import collections
class Solution:
    def snakesAndLadders(self, board):
        board.reverse()

        self.length = len(board)
        queue = collections.deque([(1,0)])
        visited = set()

        while len(queue) > 0:
            square, moves = queue.popleft()

            for i in range(1, 7):
                nextSquare = square + i

                r,c = self.intToPos(nextSquare)

                if board[r][c] != -1:
                    nextSquare = board[r][c]

                if nextSquare == self.length * self.length:
                    return moves + 1
                
                if nextSquare not in visited:
                    visited.add(nextSquare)
                    queue.append((nextSquare, moves + 1))
        return -1


    # convert integer to r,c position on board
    def intToPos(self, square):
        r = (square - 1) // self.length
        c = (square - 1) % self.length
        
        # if we are on odd row, we are going in reverse direction
        if r % 2 == 1:
            c = self.length - 1 - c
        return [r,c]
    
board = [[-1,-1,-1,-1,-1,-1],
         [-1,-1,-1,-1,-1,-1],
         [-1,-1,-1,-1,-1,-1],
         [-1,35,-1,-1,13,-1],
         [-1,-1,-1,-1,-1,-1],
         [-1,15,-1,-1,-1,-1]]

sln = Solution()
print(sln.snakesAndLadders(board))