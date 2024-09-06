import collections
import math 
class Solution:
    def evalRPN(self, tokens):
        operators = {"+", "-", "*", "/"}

        stack = collections.deque(tokens)

        
        numbers = collections.deque([])
        while len(stack) > 0:
            token = stack.popleft()

            if token in operators:
                # evaluate
                secondNum = numbers.popleft()
                firstNum = numbers.popleft()
                
                if token == "+":
                    res = firstNum + secondNum
                elif token == "-":
                    res = firstNum - secondNum
                elif token == "*":
                    res = firstNum * secondNum
                else:
                    res = int(firstNum / secondNum)
                
                numbers.appendleft(res)
                    
            else:
                num = int(token)
                numbers.appendleft(num)

        return numbers[-1]
        
tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
sln = Solution()
print(sln.evalRPN(tokens))         
