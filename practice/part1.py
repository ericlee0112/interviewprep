'''

list of orders in the format of [duration, time]

calculate lowest average wait time of your customers to recieve their orders


sort based on time when order was placed and duration

orders = [[4,1], [5,2], [2,3]]


waittime for first customer = 4
driver will be available at t = (4 + 1) = 5

waititme for second customer = (5 - 2) + 5 = 8
driver will be available at t = 5 + duration (5) = 10

waittime for third customer = (10 - 3) + 2 = 9
driver will be avilable at t = 10 + duration (2) = 12


'''

def part1(orders):
    orders = sorted(orders, key = lambda x : (x[1], x[0]))

    totalWaitTimes = 0
    timeWhenDriverIsAvailable = 0

    for duration, time in orders:

        timeWhenOrderIsExecuted = max(timeWhenDriverIsAvailable, time)

        timeWhenOrderIsFulfilled = timeWhenOrderIsExecuted + duration

        timeThatCustomerNeedsToWait = timeWhenOrderIsFulfilled - time

        totalWaitTimes += timeThatCustomerNeedsToWait

        timeWhenDriverIsAvailable = timeWhenOrderIsFulfilled

    return totalWaitTimes / len(orders)

orders = [[4,1], [5,2], [2,3]]
print(part1(orders))