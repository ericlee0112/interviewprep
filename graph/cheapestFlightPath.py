'''
Cheapest Flight Path
There are n airports, labeled from 0 to n - 1, which are connected by some flights. 
You are given an array flights where flights[i] = [from_i, to_i, price_i] represents a one-way flight from airport from_i to airport to_i with cost price_i. 
You may assume there are no duplicate flights and no flights from an airport to itself.

You are also given three integers src, dst, and k where:

src is the starting airport
dst is the destination airport
src != dst
k is the maximum number of stops you can make (not including src and dst)
Return the cheapest price from src to dst with at most k stops, or return -1 if it is impossible.

Input: n = 4, flights = [[0,1,200],[1,2,100],[1,3,300],[2,3,100]], src = 0, dst = 3, k = 1

Output: 500

0 -> 1 -> 3
     | 
     2  
      
minimum spanning trees

'''
import collections
import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        hashmap = {}
        for i in range(n):
            hashmap[i] = []

        for (a,b,cost) in flights:
            hashmap[a].append((cost, b))

        visited = set()
        visited.add(src)
        minheap = [[0, -1, src]]

        totalCost = 0

        while len(minheap) > 0:
            cost, stops, airport = heapq.heappop(minheap)

            if stops == k and airport != dst:
                visited.clear()
                continue
            
            totalCost = cost
            visited.add(airport)
            if airport == dst:
                break
            # add neighbours
            for (nextFlightCost, nextAirport) in hashmap[airport]:
                if nextAirport not in visited:
                    heapq.heappush(minheap, (cost + nextFlightCost, stops + 1, nextAirport))
        if airport == dst:
            return totalCost
        else:
            return -1

sln = Solution()
n = 13
flights = [[11,12,74],[1,8,91],[4,6,13],[7,6,39],[5,12,8],[0,12,54],[8,4,32],[0,11,4],[4,0,91],[11,7,64],[6,3,88],[8,5,80],[11,10,91],[10,0,60],[8,7,92],[12,6,78],[6,2,8],[4,3,54],[3,11,76],[3,12,23],[11,6,79],[6,12,36],[2,11,100],[2,5,49],[7,0,17],[5,8,95],[3,9,98],[8,10,61],[2,12,38],[5,7,58],[9,4,37],[8,6,79],[9,0,1],[2,3,12],[7,10,7],[12,10,52],[7,2,68],[12,2,100],[6,9,53],[7,4,90],[0,5,43],[11,2,52],[11,8,50],[12,4,38],[7,9,94],[2,7,38],[3,7,88],[9,12,20],[12,0,26],[10,5,38],[12,8,50],[0,2,77],[11,0,13],[9,10,76],[2,6,67],[5,6,34],[9,7,62],[5,3,67]]
src = 10
dst = 1
k = 10
print(sln.findCheapestPrice(n, flights, src, dst, k))