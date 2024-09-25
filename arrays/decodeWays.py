import collections

class InefficientSolution:
    def numDecodings(self, s: str) -> int:
        self.s = s
        self.ans = 0
        self.traverse(0)
        return self.ans
    
    def traverse(self, index):
        if index == len(self.s):
            self.ans += 1
        elif self.s[index] != "0":
            # check the two possiblilities
            if index < len(self.s) - 1 and int(self.s[index:index+2]) < 27:
                self.traverse(index + 1)
                self.traverse(index + 2)
            else:
                self.traverse(index + 1)

class BetterSolutionUsingMemoization:
    def numDecodings(self, s):
        self.s = s
        self.memo = collections.defaultdict(int)
        self.traverse(0)
    
    def traverse(self, index):
        if index in self.memo:
            return self.memo[index]
        elif index == len(self.s) or index == len(self.s) - 1:
            return 1
        else:
            if self.s[index] == "0":
                return 0
            elif index < len(self.s) - 1 and int(self.s[index:index+2]) < 27:
                ans = self.traverse(index + 1) + self.traverse(index + 2)
            else:
                ans = self.traverse(index + 1)
            self.memo[index] = ans
            return ans


