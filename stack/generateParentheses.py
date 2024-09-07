class Solution:
    def generateParenthesis(self, n):
        self.res = []
        self.traverse(n - 1, n, "(")
        return self.res

    def traverse(self, leftBrackets, rightBrackets, parentheses):
        if leftBrackets == 0 and rightBrackets == 0:
            self.res.append(parentheses)
            return
        else:
            if leftBrackets == 0:
                self.traverse(leftBrackets, rightBrackets - 1, parentheses + ")") 
            elif leftBrackets < rightBrackets:
                self.traverse(leftBrackets - 1, rightBrackets, parentheses + "(") 
                self.traverse(leftBrackets, rightBrackets - 1, parentheses + ")") 
            else:
                self.traverse(leftBrackets - 1, rightBrackets, parentheses + "(") 
                
                

sln = Solution()
print(sln.generateParenthesis(3))