'''
given two strings word1 and word2, reutrn min number of steps to make word1 == word2

in one step, you can delete exactly one char in either string

sea, eat
output = 2
sea -> ea
eat -> ea


e.g. abc, cba
2d dp array
   " a b c
"  0 1 2 3
c  1 2 3 2
b  2 3 2 3
a  3 2 3 4 
'''
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        cols = len(word1)
        rows = len(word2)
        # n = cols
        # m = rows
        dp = [[0 for _ in range(cols + 1)] for _ in range(rows + 1)]

        for c in range(cols + 1):
            dp[0][c] = c
        
        for r in range(rows + 1):
            dp[r][0] = r
        
        for r in range(1, rows + 1):
            for c in range(1, cols + 1):
                if word1[c - 1] == word2[r - 1]:
                    dp[r][c] = dp[r - 1][c - 1]
                else:
                    dp[r][c] = 1 + min(dp[r - 1][c], dp[r][c - 1])
        
        return dp[-1][-1]

