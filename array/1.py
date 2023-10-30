# two sum
class Solution:
    def twoSum(self, nums, target):
        # initailize hashmap
        hashmap = {} # key = diff, val = index
        # loop through nums
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hashmap:
                return [hashmap[diff], i]
            else:
                hashmap[nums[i]] = i
        

sln = Solution()
nums = [2,7,11,15]
target = 9
print(sln.twoSum(nums, target))