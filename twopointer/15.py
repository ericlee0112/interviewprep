# three sum
'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.

[-1,0,1,2,-1,-4]
[-4,-1,-1,0,1,2]

'''
nums = [-1,0,1,2,-1,-4]

class Solution:
    def threeSum(self, nums):
        nums.sort()
        self.ans = []

        for i in range(len(nums)):
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            else:
                self.twoSum(nums[i], nums[i + 1:])
        
        return self.ans
    
    def twoSum(self, firstNum, nums):
        left = 0
        right = len(nums) - 1
        while left < right:
            total = firstNum + nums[left] + nums[right]
            if total == 0:
                self.ans.append([firstNum, nums[left], nums[right]])
                
                left += 1
                right - 1
                while nums[left] == nums[left - 1] and left < right:
                    left += 1
                while right < len(nums) - 1 and nums[right] == nums[right + 1] and left < right:
                    right -= 1

            elif total > 0:
                right -= 1
            else:
                left += 1

        
sln = Solution()
print(sln.threeSum(nums))