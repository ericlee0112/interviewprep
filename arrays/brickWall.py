'''
https://leetcode.com/problems/brick-wall/description/

There is a rectangular brick wall in front of you with n rows of bricks. The ith row has some number of bricks each of the same height (i.e., one unit) but they can be of different widths. The total width of each row is the same.

Draw a vertical line from the top to the bottom and cross the least bricks. If your line goes through the edge of a brick, then the brick is not considered as crossed. You cannot draw a line just along one of the two vertical edges of the wall, in which case the line will obviously cross no bricks.

Given the 2D array wall that contains the information about the wall, return the minimum number of crossed bricks after drawing such a vertical line.

Input: wall = [[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]
Output: 2

Input: wall = [[1],[1],[1]]
Output: 3

'''

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        # keep track of the frequencies of each wall cut
        edge_frequences = collections.defaultdict(int)

        for row in wall:
            brickLength = 0
            for i in range(len(row) - 1):
                brick = row[i]
                brickLength += brick
                edge_frequences[brickLength] += 1

        

        # iterate through each edge index and find the edge index with the most frequencies
        mostFrequencies = 0
        for k,v in edge_frequences.items():
            mostFrequencies = max(mostFrequencies, v)

        # return len(wall) - mostFrequencies
        return len(wall) - mostFrequencies
