# top k frequent elements
from heapq import heappop, heappush, heapify
import collections

class Solution:
    def topKFrequent(self, nums, k):    
        hashmap = collections.defaultdict(int)

        for num in nums:
            hashmap[num] += 1

        pairs = []
        
        # turn key,val into tuples 
        for key,val in hashmap.items():
            pairs.append((key,val))
        
        pairs.sort(key=lambda tuple: -tuple[1])

        return [pairs[i][0] for i in range(k)]

    
#Input: nums = [1,1,1,2,2,3], k = 2
#Output: [1,2]

nums = [1,1,1,1,1,1,1,2,2,2,2,3,3]
k = 2


class BetterSolution:
    def topKFrequent(self, nums, k):
        hashmap = collections.defaultdict(int)

        for num in nums:
            hashmap[num] += 1

        heap = []
        heapify(heap)

        for key,val in hashmap.items():
            # modification to turn it into maxheap, since by default heap is minheap in python
            heappush(heap, (-1*val,key))
        
        
        ans = []
        for i in range(k):
            (val,key) = heappop(heap)
            ans.append(key)
        
        return ans
            


betterSolution = BetterSolution()
betterRes = betterSolution.topKFrequent(nums, k)
print(betterRes)



class BestSolution:
    def topKFrequent(self, nums, k):
        bucket_array = [ [] for i in range(len(nums) + 1)]

        freqmap = collections.defaultdict(int)
        for num in nums:
            freqmap[num] += 1
        
        for (key,val) in freqmap.items():
            bucket_array[val].append(key)

        ans = []
        for i in range(len(bucket_array) - 1, -1, -1):
            keys = bucket_array[i]
            for key in keys:
                ans.append(key)
                k -= 1
            
            if k == 0:
                return ans

        return ans

bestSolution = BestSolution()
bestResult = bestSolution.topKFrequent(nums, k)
print(bestResult)
