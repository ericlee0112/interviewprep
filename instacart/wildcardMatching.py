import collections


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        rows = len(s)
        cols = len(p)

        dp = [[False for _ in range(cols + 1)] for _ in range(rows + 1)]

        dp[0][0] = True

        for j in range(1, cols + 1):
            if p[j - 1] == "*":
                dp[0][j] = dp[0][j - 1]

        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                if s[i - 1] == p[j - 1] or p[j - 1] == "?":
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == "*":
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
        
        return dp[-1][-1]
    
s = "aa"
p = "*"
sln = Solution()
print(sln.isMatch(s,p))

