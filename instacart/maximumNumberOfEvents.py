'''
given an array of events where events[i] = [startDayI, endDayI]
you can attend an event on any day between its start and end day

return the max number of events you can attend
'''

events = [ [1,2], [2,6], [2,4], [5,8] ]

def solution(events):
    if len(events) < 2:
        return len(events)
    # sort based on endDay
    events = sorted(events, key = lambda x : x[1])

    res = [events[0]]
    
    numberOfEventsICanAttend = 1
    
    
    for i in range(1, len(events)):
        endOfLastEvent = res[-1][1]
        
        startOfIncomingEvent = events[i][0]

        if startOfIncomingEvent >= endOfLastEvent:
            res.append(events[i])
            numberOfEventsICanAttend += 1

    return res            
        



'''
You are given an array of events where events[i] = [startDayi, endDayi]. Every event i starts at startDayi and ends at endDayi.

You can attend an event i at any day d where startTimei <= d <= endTimei. You can only attend one event at any time d.

Return the maximum number of events you can attend.

 
Example 1:
Input: events = [[1,2],[2,3],[3,4]]
Output: 3
Explanation: You can attend all the three events.
One way to attend them all is as shown.
Attend the first event on day 1.
Attend the second event on day 2.
Attend the third event on day 3.

Example 2:
Input: events= [[1,2],[2,3],[3,4],[1,2]]
Output: 4

'''
import heapq

def maxEvents(events):
    # sort events based on start day
    events = sorted(events, key = lambda x : (x[0], x[1]))

    # get the last day 
    lastDay = max([event[1] for event in events])

    # use minheap to keep track of ongoing events
    minheap = []
    index = 0
    maxNumberOfEventsThatCanBeAttended = 0
    currentDay = 1

    while currentDay <= lastDay:
        # add ongoing events that are starting on currentday
        while index < len(events) and events[index][0] <= currentDay:
            heapq.heappush(minheap, events[index][1])
            index += 1
        
        # remove events that have passed that we can no longer attend
        while len(minheap) < 0 and minheap[0] < currentDay:
            heapq.heappop(minheap)
        
        if len(minheap) > 0:
            heapq.heappop(minheap)
            maxNumberOfEventsThatCanBeAttended += 1
        
        currentDay += 1
    
    return maxNumberOfEventsThatCanBeAttended
                

events = [[1,4],[4,4],[2,2],[3,4],[1,1]]

print(maxEvents(events))

events = [ [1,2], [2,6], [2,4], [5,8] ]

print(maxEvents(events))

print(solution(events))

            