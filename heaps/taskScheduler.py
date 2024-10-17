
import heapq
import collections

class Solution:
    def leastInterval(self, tasks, n):
        queue = collections.deque([])
        hashmap = collections.defaultdict(int)
        for t in tasks:
            hashmap[t] += 1
        
        maxheap = []
        for freq in hashmap.values():
            heapq.heappush(maxheap, (-freq))
        
        t = 0

        while len(maxheap) > 0 or len(queue) > 0:
            t += 1

            if len(maxheap) > 0:
                freq = heapq.heappop(maxheap)
                freq = freq * -1
                
                freq -= 1

                if freq > 0:
                    queue.append((freq, t + n))
            
            if len(queue) > 0 and queue[0][1] == t:
                freq, timeWhenWeCanExecuteTaskAgain = queue.popleft()
                heapq.heappush(maxheap, (-freq))
        
        return t


                

sln = Solution()
tasks = ["A", "A", "A", "A", "B", "B", "B", "C", "C"]
n = 2
print(sln.leastInterval(tasks, n))

ABCABCA
