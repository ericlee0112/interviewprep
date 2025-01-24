'''
[-6, -5, -4, -3, -2, 0, 1]

[1,1,1,1,1,0,1,1]

'''
import heapq

def solution(queries):
    lastHouse = max(queries)
    firstHouse = min(queries)
    
    minheap = []
    
    output = []
    for num in queries:
        heapq.heappush(minheap, num)
        
        # insert here
        maxSequence = 0
        sequence = 0
        prevHouse = None
        usedHouses = []

        while len(minheap) > 0:
            house = heapq.heappop(minheap)
            if prevHouse == None or abs(prevHouse - house) == 1:
                prevHouse = house
                sequence += 1
                heapq.heappush(usedHouses, house)
            else:
                maxSequence = max(sequence, maxSequence)
                sequence = 1
                prevHouse = house
                heapq.heappush(usedHouses, house)
        
        maxSequence = max(sequence, maxSequence)
        
        minheap = usedHouses
        
        output.append(maxSequence)
        
    return output