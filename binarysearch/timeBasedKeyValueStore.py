
class TimeMap:
    def __init__(self):
        self.hashmap = {}
    
    def set(self, key, val, timestamp):
        if key not in self.hashmap:
            self.hashmap[key] = []
        self.hashmap[key].append((val, timestamp))
    
    def get(self, key, timestamp):
        if key not in self.hashmap:
            return ""
        
        listOfValues = self.hashmap[key]

        bestValueToBeReturned = self.binarySearch(listOfValues, timestamp)
        return bestValueToBeReturned
    
    def binarySearch(self, listOfValues, timestamp):
        left = 0
        right = len(listOfValues) - 1

        bestPossibleValueThatWeCanReturn = ""

        while left <= right:
            mid = (left + right) // 2
            if listOfValues[mid][1] <= timestamp:
                bestPossibleValueThatWeCanReturn = listOfValues[mid][0]
                left = mid + 1
            else:
                right = mid - 1
        return bestPossibleValueThatWeCanReturn
    