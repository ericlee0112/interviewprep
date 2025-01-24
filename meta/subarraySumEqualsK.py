''''
given array of integers, and an int k, return total number of continuous subarrays whose sum equals to k


nums = [1,1,1], k = 2
output = 2

nums = [1,2,3], k = 3
output = 2

brute force = O(n2)

solution: use prefix sum

hashmap 
prefix sum -> count

'''
import collections
def solution(nums, k):
    hashmap = collections.defaultdict(int)
    hashmap[0] = 1

    subArraySum = 0
    subarraysThatEqualK = 0
    for i in range(len(nums)):
        subArraySum += nums[i]
        prefix = subArraySum - k
        
        previousSubarrays = hashmap[prefix]
        subarraysThatEqualK += previousSubarrays
        
        hashmap[subArraySum] += 1
    
    return subarraysThatEqualK

        
nums = [1,-1,1,1,1,1]
k = 3
print(solution(nums, k))