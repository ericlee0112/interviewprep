class Solution:
    def bestClosingTime(self, customers):
        n = len
        prefixN = [0 for _ in range(len(customers) + 1)]
        postY = [0 for _ in range(len(customers) + 1)]

        for i in range(1, len(customers) + 1):
            prefixN[i] = prefixN[i - 1]
            if customers[i - 1] == "N":
                prefixN[i] += 1
        
        for i in range(len(customers) - 1, -1, -1):
            postY[i] = postY[i + 1]
            if customers[i] == "Y":
                postY[i] += 1


        minPenaltySoFar = float('inf')
        bestTime = 0

        for i in range(len(customers) + 1):
            penalty = postY[i] + prefixN[i]
            if penalty < minPenaltySoFar:
                minPenaltySoFar = penalty
                bestTime = i
            
        return bestTime

       

           

        
sln = Solution()
customers = "YN"
print(sln.bestClosingTime(customers))
        
