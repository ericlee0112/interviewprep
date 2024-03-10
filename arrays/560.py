# subarray sum equals k 
# https://leetcode.com/problems/subarray-sum-equals-k/
'''
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2

Example 2:

Input: nums = [1,2,3], k = 3
Output: 2

 
Solution:
use hashmap to keep track of prefix sums from (i,j)

sum(i,j) = sum(0,j) - sum(0,i)
'''
import collections
def subarraySums(nums, k):
    ans = 0
    prefix_hashmap = collections.defaultdict(int)
    prefix_hashmap[0] = 1
    
    totalsum = 0

    for i in range(len(nums)):
        totalsum += nums[i]
        prefixsum = totalsum - k
        ans += prefix_hashmap[prefixsum]
        prefix_hashmap[totalsum] += 1
    return ans


nums = [1,-1,1,1,1,1]
k = 3
print(subarraySums(nums, k))