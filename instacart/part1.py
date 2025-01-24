'''
for a given array of orders with the format [duration, time]

calculate lowest average wat time of your customers to receive their orders

e.g.
[4,1], [5,2], [2,3]
first order is placed at t=1, and takes 4 minutes to fulfill, this customer will need to wait 4 minutes
second order is placed at t=2, and takes 5 minutes to fulfill. we still need 3 minutes to fulfill first order, and an additional 5 minutes, so 8 minutes total
third order is placed at t=3, and takes 2 minutes to fulfill. 2 minutes left on first order, 5 minutes yet to be fulfilled on second order, and then 2 more minutes for this third order

total = (4 + 8 + 9) / 3 = 7
'''

def getAverageWaitTime(orders):
    # sort orders by time
    orders = sorted(orders, key = lambda x : (x[1], x[0]))
    print(orders)

    timeWhenDriverIsIdle = orders[0][0] + orders[0][1]

    waitTimes = [orders[0][0]]

    for i in range(1, len(orders)):
        order = orders[i]
        timeToFulfillOrderI = order[0]
        timeWhenOrderIWasPlaced = order[1]

        timeToWaitUntilDriverBecomesIdle = timeWhenDriverIsIdle - timeWhenOrderIWasPlaced

        waitTimeForOrderI = (timeToWaitUntilDriverBecomesIdle + timeToFulfillOrderI)

        timeWhenDriverIsIdle += (timeToFulfillOrderI)

        waitTimes.append(waitTimeForOrderI)
    
    return waitTimes

def alternativeSolution(orders):
    # sort orders by time
    orders = sorted(orders, key = lambda x : x[1])  

    timeUntilDriverIsAvailable = 0
    waitTimes = []
    totalWaitTime = 0

    for (duration, time) in orders:
        startTime = max(timeUntilDriverIsAvailable, time)

        timeUntilDriverIsAvailable = startTime + duration

        waitTimeForCustomer = timeUntilDriverIsAvailable - time

        waitTimes.append(waitTimeForCustomer)
        totalWaitTime += (waitTimeForCustomer)
    

    return waitTimes
    





    

orders = [[4,1], [5,2], [2,3], [3,5], [4,7]]
# [4,8,9,]
print(getAverageWaitTime(orders))
print(alternativeSolution(orders))


