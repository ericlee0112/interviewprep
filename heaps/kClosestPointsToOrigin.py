import heapq
import math

def kClosest(points, k):
    heap = []
    res = []
    for i in range(len(points)):
        x = points[i][0]
        y = points[i][1]

        distance = calculateDistance(x,y)

        heapq.heappush(heap, (distance, i))
    
    for i in range(k):
        (distance, index) = heapq.heappop(heap)
        res.append(points[index])

    return res

def calculateDistance(x,y):
    return math.sqrt(math.pow(abs(x),2) + math.pow(abs(y), 2))
 