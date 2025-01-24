'''

gas = [1,2,3,4], cost = [2,2,4,1]

ans = 3

[1,2,3,4,1,2,3,4]
[2,2,4,1,2,2,4,1]

loop from 0 to len(gas)
    at every index, perform simulation
    the simulation is considered successful if we can go from index i to i + len(gas)

'''

class Solution:
    def canCompleteCircuit(self, gasList, costList):
        self.circuitLength = len(gasList)
        self.gasList = gasList + gasList
        self.costList = costList + costList

        for i in range(self.circuitLength):
            res = self.simulate(i)
            if res:
                return i
        return -1

    def simulate(self, i):
        end = i + self.circuitLength
        gasTank = 0

        while i < end:
            gas = self.gasList[i]
            gasTank += gas
            cost = self.costList[i]
            if gasTank < cost:
                return False
            else:
                gasTank -= cost
                i += 1
        
        return True


