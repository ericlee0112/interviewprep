# https://leetcode.com/problems/brick-wall/description/
import collections

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:

        edge_frequencies = collections.defaultdict(int)
        
        for row in wall:
            # process each row
            brick_length = 0
            for i in range(len(row) - 1):
                brick = row[i]
                brick_length += brick
                edge_frequencies[brick_length] += 1
        
        
        # get the largest number in cut frequencies
        most_edges = 0
        for v in edge_frequencies.values():
            most_edges = max(most_edges, v)
        
        return len(wall) - most_edges