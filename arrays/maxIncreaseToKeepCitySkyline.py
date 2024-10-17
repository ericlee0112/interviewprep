class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        numOfRows = len(grid)
        numOfCols = len(grid[0])
        northSouthViewMax = [0 for _ in range(numOfCols)]
        eastWestViewMax = [0 for _ in range(numOfRows)]

        for i in range(numOfRows):
            rowMax = max(grid[i])
            eastWestViewMax[i] = rowMax
        
        for j in range(numOfCols):
            column = [grid[i][j] for i in range(numOfRows)]
            colMax = max(column)
            northSouthViewMax[j] = colMax
        
        ans = 0

        for i in range(numOfRows):
            for j in range(numOfCols):
                threshold = min(northSouthViewMax[j], eastWestViewMax[i])
                if grid[i][j] < threshold:
                    ans += (threshold - grid[i][j])
        return ans



grid = [[3,0,8,4],
        [2,4,5,7],
        [9,2,6,3],
        [0,3,1,0]]
sln = Solution()
print(sln.maxIncreaseKeepingSkyline(grid))