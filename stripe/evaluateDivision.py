import collections

class Solution:
    def calcEquation(self, equations, values, queries):
        self.adjacencyMap = collections.defaultdict(list)
        for i in range(len(equations)):
            numerator = equations[i][0]
            denominator = equations[i][1]
            numeratorOverDenominatorResult = values[i]
            denominatorOverNumeratorResult = 1 / values[i]
            self.adjacencyMap[numerator].append((denominator, numeratorOverDenominatorResult))
            self.adjacencyMap[denominator].append((numerator, denominatorOverNumeratorResult))

        output = []
        for (numerator, denominator) in queries:
            if numerator not in self.adjacencyMap or denominator not in self.adjacencyMap:
                res = -1.0
            else:
                res = self.dfs(numerator, denominator)
            output.append(res)
        
        return output
    
    def dfs(self, numerator, denominator):
        # travel from numerator to denominator
        queue = collections.deque([(numerator, 1)])
        seen = set()
        while len(queue) > 0:
            num, product = queue.popleft()
            if num == denominator:
                return product

            neighbours = self.adjacencyMap[num]
            for (neighbouringNode, pathProduct) in neighbours:
                if neighbouringNode not in seen:
                    seen.add(neighbouringNode)
                    nextProduct = product * pathProduct
                    queue.append((neighbouringNode, nextProduct))
        
        return -1.0

equations = [["a","b"],["b","c"]]
values = [2.0,3.0]
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
sln = Solution()
print(sln.calcEquation(equations, values, queries))