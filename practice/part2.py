'''
for a given k calculate minimum number of shoppers needed
so that avg customer wait time does not exceed k

if given k is not possible, return 0

the sum of durations / number of orders should not be greater than k, if it is, then it is impossible

orders = [[4,1], [5,2], [2,3]]



'''
import heapq

def part2(orders, k):
    orders = sorted(orders, key = lambda x : (x[1], x[0]))
    sumOfDurations = sum([order[0] for order in orders])
    if sumOfDurations / len(orders) > k:
        return 0
    
    numberOfShoppers = 0

    averageWaitTime = float('inf')

    while averageWaitTime > k:
        numberOfShoppers += 1
        simulatedWaitTime = simulate(orders, numberOfShoppers)
        averageWaitTime = min(averageWaitTime, simulatedWaitTime)


    return averageWaitTime

def simulate(orders, numberOfShoppers):
    print("simuating with " + str(numberOfShoppers) + " shoppers")
    # initalize minheap and place shoppers times when they are available
    minheap = []
    for _ in range(numberOfShoppers):
        minheap.append(0)
    
    waitTimes = 0
    
    for (duration, time) in orders:
        timeWhenDriverIsAvailable = heapq.heappop(minheap)

        timeWhenOrderIsExecuted = max(timeWhenDriverIsAvailable, time)

        timeWhenOrderIsFulfilled = timeWhenOrderIsExecuted + duration

        timeThatCustomerNeedsToWait = timeWhenOrderIsFulfilled - time
        print(timeThatCustomerNeedsToWait)

        waitTimes += timeThatCustomerNeedsToWait

        timeWhenDriverIsAvailable = timeWhenOrderIsFulfilled

        heapq.heappush(minheap, timeWhenDriverIsAvailable)
    
    return waitTimes / len(orders)

orders = [[4,1], [5,2], [2,3]]
k = 5

print(part2(orders,k))