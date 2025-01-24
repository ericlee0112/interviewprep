
'''
orders = [ [4,1], [5,2], [2,3] ]

○ First order is placed at time 1 and takes 4 time units to fulfill. The customer needs to wait 4 time units
○ Second order is placed at time 2. The customer needs to wait 3 time units for you to finish the first order. Their order takes 5 time units. The customer needs to wait 8 time units
○ Third order is placed at time 3. The customer needs to wait 7 time units for you to finish the first two orders. Their order takes 2 time units. The customer needs to wait 9 time units
○ The average wait time is (4+8+9)/3 = 7.0 time units


totalWaitTimes = 0
timeUntilDriverIsIdle = 0



'''
import collections
import heapq

def part1(orders):
    orders = sorted(orders, key = lambda x: x[1])
    totalWaitTimes = []
    timeUntilDriverIsIdle = 0

    for i in range(len(orders)):
        timeOfExecution = orders[i][1]
        timeToFulfillOrder = orders[i][0]
        if i == 0:
            totalWaitTimes.append(timeToFulfillOrder)
            timeUntilDriverIsIdle = timeOfExecution + timeToFulfillOrder
        else:
            # total wait time for this order 
            timeToWaitUntilDriverBecomesIdle = timeUntilDriverIsIdle - timeOfExecution
            waitTimeToFulfillOrder = timeToFulfillOrder + timeToWaitUntilDriverBecomesIdle
            totalWaitTimes.append(waitTimeToFulfillOrder)
            timeUntilDriverIsIdle += timeToFulfillOrder

    return totalWaitTimes



def part2(orders, k):
    orders = sorted(orders, key = lambda x: x[1])

    # the number of shoppers is bounded between 1 and len(orders)
    if sum(duration for duration, _ in orders) / len(orders) > k:
        return

    averageWaitTime = float('inf')
    numberOfShoppers = 0
    while averageWaitTime > k:
        numberOfShoppers += 1
        simulatedWaitTime = simulate(orders, numberOfShoppers)
        averageWaitTime = min(averageWaitTime, simulatedWaitTime)
   
    return numberOfShoppers
    
def part2WithBinarySearch(orders, k):
    orders = sorted(orders, key = lambda x: x[1])

    # the number of shoppers is bounded between 1 and len(orders)
    if sum(duration for duration, _ in orders) / len(orders) > k:
        return

    left = 1
    right = len(orders)
    while left < right:
        midPoint = (right + left) // 2
        simulatedWaitTime = simulate(orders, midPoint)
        print(simulatedWaitTime)
        if simulatedWaitTime > k:
            left = midPoint + 1
        else:
            right = midPoint 

    return left


def simulate(orders, numberOfShoppers):
    minheap = []
    for _ in range(numberOfShoppers):
        minheap.append(0)

    totalWaitTimes = 0
    for order in orders:
        print(minheap)
        timeOrderWasPlaced = order[1]
        timeToFulfillOrder = order[0]

        timeAtWhichDriverIsAvailable = heapq.heappop(minheap)

        timeWhenOrderIsExecuted = max(timeOrderWasPlaced, timeAtWhichDriverIsAvailable)

        timeToWaitForOrderToBeExecuted = (timeWhenOrderIsExecuted - timeOrderWasPlaced)

        totalWaitTimeForOrder = timeToWaitForOrderToBeExecuted + timeToFulfillOrder

        totalWaitTimes += totalWaitTimeForOrder

        timeAtWhichDriverIsAvailable += (totalWaitTimeForOrder)

        heapq.heappush(minheap, timeAtWhichDriverIsAvailable)

    return totalWaitTimes / len(orders)


ordersPart2 = [ [4,1], [5,2], [2,3], [3,5], [6,9] ]
k = 5
print(part2WithBinarySearch(ordersPart2, k))