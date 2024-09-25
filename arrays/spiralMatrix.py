class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        startingRow = 0
        startingCol = 0
        endingRow = len(matrix)
        endingCol = len(matrix[0])

        ans = []

        while startingRow < endingRow and startingCol < endingCol:
            # go right (columns)
            for j in range(startingCol, endingCol):
                ans.append(matrix[startingRow][j])
            startingRow += 1

            # go down
            for i in range(startingRow, endingRow):
                ans.append(matrix[i][endingCol - 1])
            endingCol -= 1

            # check if startingRow and startingCol are matching endingRow and endingCol
            if  (startingRow < endingRow and startingCol < endingCol):
                    

                # go left
                for j in range(endingCol - 1, startingCol - 1, -1):
                    ans.append(matrix[endingRow - 1][j])
                endingRow -= 1

                # go up
                for i in range(endingRow - 1, startingRow - 1, -1):
                    ans.append(matrix[i][startingCol])      
                startingCol += 1
        return ans
