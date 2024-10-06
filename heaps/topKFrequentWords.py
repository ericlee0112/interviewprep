import heapq
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        heap = []
        hashmap = collections.defaultdict(int)
        for word in words:
            hashmap[word] += 1
        
        for word, freq in hashmap.items():
            heapq.heappush(heap, (-1 * freq, word))
        
        ans = []
        for i in range(k):
            freq, word = heapq.heappop(heap)
            ans.append((freq, word))
        
        ans.sort()
        
        return [a[1] for a in ans]