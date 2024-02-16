'''
product of array except self 
https://leetcode.com/problems/product-of-array-except-self/description/

[1,2,3,4]

from left to right
algorithm:
left = []
for i in range(len(nums))
    if i == 0:
        left.append(1)
    else:
        left.append(left[i - 1]*nums[i - 1])

[1,1,2,6]

from right to left
algorithm:
right = [0 for i in range(len(nums))]
for i in range(len(nums) - 1, -1, -1):
    if i == len(nums) - 1:
        right[i] = 1
    else:
        right[i] = right[i + 1] * nums[i + 1]

[24,12,4,1]

[24,12,8,6]



'''

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = []
        right = [0] * len(nums)

        # build the left list
        for i in range(len(nums)):
            if i == 0:
                left.append(1)
            else:
                left.append(left[i-1]*nums[i-1])
        
        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                right[i] = 1
            else:
                right[i] = right[i + 1] * nums[i + 1]

        final = []
        for i in range(len(nums)):
            final.append(left[i]*right[i])

        return final