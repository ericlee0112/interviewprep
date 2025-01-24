'''

Problem: Given an `n x n` binary matrix grid, where each 1 represents a wall and 0 represents a clear path, 
find the shortest path from the top-left corner (0,0) to the bottom-right corner (n-1,n-1). 
You can only move horizontally and vertically.

solution: use bfs (queue)
'''
import collections
def solution(matrix):
    queue = collections.deque([(0,0,0)])
    rows = len(matrix)
    cols = len(matrix[0])

    seen = set()

    neighbours = [0,1,0,-1,0]

    while len(queue) > 0:
        distance, i, j = queue.popleft()
        seen.add((i,j))

        if i == rows - 1 and j == cols - 1:
            return distance
        
        # add neighbours
        for k in range(len(neighbours) - 1):
            newI = i + neighbours[k]
            newJ = j + neighbours[k + 1]
            if newI >= 0 and newI < rows and newJ >= 0 and newJ < cols and (newI, newJ) not in seen and matrix[newI][newJ] == 0:
                queue.append((distance + 1, newI, newJ))
        
    return -1

matrix = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]]




def hasPath(maze, start, destination):
    queue = collections.deque([(start)])

    seen = set()

    neighbours = [0,1,0,-1,0]

    while len(queue) > 0:
        i,j = queue.popleft()
        print((i,j))
        if [i,j] == destination:
            return True
        for k in range(len(neighbours) - 1):
            newI = i + neighbours[k]
            newJ = j + neighbours[k + 1]
            if newI >= 0 and newI < len(maze) and newJ >= 0 and newJ < len(maze[0]) and (newI, newJ) not in seen:
                print((newI, newJ))
                seen.add((newI, newJ))
                queue.append((newI, newJ))


    
    return False

maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]]
start = [0,4]
end = [4,4]
print(hasPath(maze, start, end))

''''
[0,0,1,0,0],
[0,0,0,0,0],
[0,0,0,1,0],
[1,1,0,1,1],
[0,0,0,0,0]]


'''