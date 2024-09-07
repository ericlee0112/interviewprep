import collections

class Solution:
    def dailyTemperatures(self, temps):
        ans = [0 for _ in range(len(temps))]

        stack = []
        for i in range(len(temps)):
            currentTemp = temps[i]
            if i == 0:
                stack.append([currentTemp,i])
            elif len(stack) > 0:
                # compare with top of stack
  
   
                while len(stack) > 0 and stack[-1][0] < currentTemp:
                    oldTemp, index = stack.pop()
                    ans[index] = (i - index)
                stack.append([currentTemp, i])
            print(stack)
        
        return ans


temps = [30,38,30,36,35,40,28]
sln = Solution()
print(sln.dailyTemperatures(temps))




