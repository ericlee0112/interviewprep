'''
you are given two strings word1 and word2

You are allowed to perform three operations on word1 an unlimited number of times:

Insert a character at any position
Delete a character at any position
Replace a character at any position

Return the minimum number of operations to make word1 equal word2.

'''

def minDistance(word1, word2):
    dp = [[float('inf') for _ in range(len(word2) + 1)] for _ in range(len(word1) + 1)]

    for i in range(len(word2) + 1):
        dp[len(word1)][i] = len(word2) - i
    
    for i in range(len(word1) + 1):
        dp[i][len(word2)] = len(word1) - i
    
    for i in range(len(word1) - 1, -1, -1):
        for j in range(len(word2) - 1, -1, -1):
            if word1[i] == word2[j]:
                dp[i][j] = dp[i + 1][j + 1]
            else:
                dp[i][j] = 1 + min(dp[i + 1][j], dp[i][j + 1], dp[i + 1][j + 1])
    
    return dp[0][0]