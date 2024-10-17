import heapq

class KthLargest:
    def __init__(self, k, nums):
        self.k = k
        self.nums = []
        for num in nums:
            heapq.heappush(self.nums, -1 * num)

    def add(self, val):
        heapq.heappush(self.nums, -1 * val)

        holdingNumbers = []

        if len(self.nums) < self.k:
            kthLargest = heapq.heappop(self.nums)
            return -1 * kthLargest
        else:
            kSmallest = heapq.nsmallest(self.k, self.nums)
            return -1 * kSmallest[-1]

kthLargest = KthLargest(3, [4,5,8,2])
print(kthLargest.add(3))