'''
Frequency of the Most Frequent Element

https://leetcode.com/problems/frequency-of-the-most-frequent-element/description/

The frequency of an element is the number of times it occurs in an array.

You are given an integer array nums and an integer k. In one operation, you can choose an index of nums and increment the element at that index by 1.

Return the maximum possible frequency of an element after performing at most k operations.

 

Example 1:

Input: nums = [1,2,4], k = 5
Output: 3
Explanation: Increment the first element three times and the second element two times to make nums = [4,4,4].
4 has a frequency of 3.
Example 2:

Input: nums = [1,4,8,13], k = 5
Output: 2
Explanation: There are multiple optimal solutions:
- Increment the first element three times to make nums = [4,4,8,13]. 4 has a frequency of 2.
- Increment the second element four times to make nums = [1,8,8,13]. 8 has a frequency of 2.
- Increment the third element five times to make nums = [1,4,13,13]. 13 has a frequency of 2.
Example 3:

Input: nums = [3,9,6], k = 2
Output: 1





[1,4,8,13]

 
'''
class BruteForceSolution:
    def maxFrequency(self, nums, k):
        # sort nums
        max_freq = 1
        nums.sort()
        for i in range(1, len(nums)):
            # look at previous nums from 0 to i - 1
            fill = 0
            freq = 1

            for j in range(i - 1, -1, -1):
                # calculate diff    
                diff = nums[i] - nums[j]
                fill += diff
                if fill > k:
                    break
                else:
                    freq += 1
            max_freq = max(max_freq, freq)
        return max_freq


class Solution:
    def maxFrequency(self, nums, k):
        max_freq = 1
        nums.sort()
        total = 0

        left = 0
        right = 0
        while right < len(nums):
            total += nums[right]
            if nums[right]*(right - left + 1) <= (total + k):
                max_freq = max(max_freq, right - left + 1)
            else:
                total -= nums[left]
                left += 1
            right += 1
        return max_freq

nums = [3,9,6]
k = 2
print(Solution().maxFrequency(nums,k))