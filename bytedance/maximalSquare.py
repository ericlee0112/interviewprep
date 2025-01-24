'''
given an mxn binary matrix filled with 0s and 1s, find the largest square containing only 1s

solution: 2d dynamic programming

create empty mxn array (this will be our cache)

go in reverse order, starting from botom right all the way to top left


'''

import math



class DynamicProgrammingSolution:
    def solution(self, matrix):
        cols = len(matrix[0])
        rows = len(matrix)
        dp = [[0 for _ in range(cols + 1)] for _ in range(rows + 1)]

        ans = 0

        for i in range(rows - 1, -1, -1):
            for j in range(cols - 1, -1, -1):
                if matrix[i][j] == "1":
                    dp[i][j] = 1 + min(dp[i + 1][j], dp[i][j + 1], dp[i + 1][j + 1])
                    ans = max(ans, dp[i][j])
        
        return math.pow(ans, 2)

matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
sln = DynamicProgrammingSolution()
print(sln.solution(matrix))