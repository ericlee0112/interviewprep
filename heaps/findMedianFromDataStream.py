'''
https://leetcode.com/problems/find-median-from-data-stream/description/

The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.

'''
import heapq

class MedianFinder:
    def __init__(self):
        # define small heap and large heap
        self.smallHeap = [] 
        heapq.heapify(self.smallHeap) # maxheap

        self.largeHeap = []
        heapq.heapify(self.largeHeap) # minheap


    def addNum(self, num):
        # by default add to smallHeap
        heapq.heappush(self.smallHeap, -1 * num)

        #largestElementInSmallHeap = self.smallHeap[0] * -1
        #smallestElementInLargeHeap = self.largeHeap[0]
        
        if len(self.smallHeap) > 0 and len(self.largeHeap) > 0 and (self.smallHeap[0] * -1) > self.largeHeap[0]:
            # pop the largest element from smallheap and add it to largeheap
            element = heapq.heappop(self.smallHeap) * -1
            heapq.heappush(self.largeHeap, element)

        # check size 
        if len(self.smallHeap) > len(self.largeHeap) + 1:
            # pop from small heap and give it to large heap     
            element = heapq.heappop(self.smallHeap) * -1
            heapq.heappush(self.largeHeap, element)

        if len(self.smallHeap) + 1 < len(self.largeHeap):
            # pop from large heap and give it to small heap
            element = heapq.heappop(self.largeHeap) * -1
            heapq.heappush(self.smallHeap, element)
        

    def findMedian(self):
        if len(self.smallHeap) > len(self.largeHeap):
            return self.smallHeap[0] * -1
        elif len(self.smallHeap) < len(self.largeHeap):
            return self.largeHeap[0]
        else:
            return ((self.smallHeap[0] * -1) + self.largeHeap[0]) / 2
        

medianFinder = MedianFinder()
medianFinder.addNum(1)
medianFinder.addNum(2)
medianFinder.addNum(3)
medianFinder.addNum(7)
print(medianFinder.findMedian())


