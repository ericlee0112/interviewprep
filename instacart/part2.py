import heapq

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
    for (duration, time) in orders:
        timeAtWhichDriverIsAvailable = heapq.heappop(minheap)

        timeWhenOrderIsExecuted = max(time, timeAtWhichDriverIsAvailable)
        
        timeWhenOrderIsFulfilled = timeWhenOrderIsExecuted + duration

        timeThatCustomerNeedsToWait = timeWhenOrderIsFulfilled - time

        totalWaitTimes += timeThatCustomerNeedsToWait

        timeAtWhichDriverIsAvailable = timeWhenOrderIsFulfilled

        heapq.heappush(minheap, timeAtWhichDriverIsAvailable)



    return totalWaitTimes / len(orders)


ordersPart2 = [ [4,1], [5,2], [2,3]]
k = 5
print(part2(ordersPart2, k))