# largest number
'''
https://leetcode.com/problems/largest-number/description/

Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

Since the result may be very large, so you need to return a string instead of an integer.

 

Example 1:

Input: nums = [10,2]
Output: "210"
Example 2:

Input: nums = [3,30,34,5,9]
Output: "9534330"

'''
import functools
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # cast nums to string array
        string_nums = [str(nums[i]) for i in range(len(nums))]
        # sort based on ascii
        sorted_string_nums = sorted(string_nums, key=functools.cmp_to_key(self.compareFunction))

        ans = ""
        for char in sorted_string_nums:
            ans += char
        if ans[0] == "0":
            return "0"
        return ans
        
    def compareFunction(self, n1,n2):
        if n1 + n2 < n2 + n1:
            return 1
        else:
            return -1
    