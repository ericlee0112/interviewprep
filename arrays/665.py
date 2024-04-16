# non decreasing array
'''
https://leetcode.com/problems/non-decreasing-array/

Given an array nums with n integers, your task is to check if it could become non-decreasing by modifying at most one element.

We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based) such that (0 <= i <= n - 2).

 

Example 1:

Input: nums = [4,2,3]
Output: true
Explanation: You could modify the first 4 to 1 to get a non-decreasing array.
Example 2:

Input: nums = [4,2,1]
Output: false
Explanation: You cannot get a non-decreasing array by modifying at most one element.

'''

def nonDecreasingArray(nums):
    swap = False

    for i in range(1, len(nums)):
        if nums[i - 1] > nums[i]:
            if swap == True or (i > 1 and i < len(nums) - 1 and nums[i - 2] > nums[i] and nums[i + 1] < nums[i - 1]):
                return False
            swap = True

    return True
    

nums1 = [4,2,3]
nums2 = [5,7,1,8]
nums3 = [-1,4,2,3]
print(nonDecreasingArray(nums1))
print(nonDecreasingArray(nums2))
print(nonDecreasingArray(nums2))