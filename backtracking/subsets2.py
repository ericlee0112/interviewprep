
'''
You are given an array nums of integers, which may contain duplicates. Return all possible subsets.

The solution must not contain duplicate subsets. You may return the solution in any order.

[1,2,2]

               [1] 1                             []1
       [1,2] 2        [1] 3               [2]2             [] 3
[1,2,2] 3  [1,2] 3                   [2,2] 3    [2] 3                 


output = [[1,2,2], [1,2], [1], [2,2], [2], []]
'''

class Solution:
    def subsets(self, nums):
        self.nums = sorted(nums)
        self.ans = []
        self.backtrack(0, [])
        return self.ans

    def backtrack(self, index, subset):
        if index == len(self.nums):
            self.ans.append(subset)
            return
    

        self.backtrack(index + 1, subset + [self.nums[index]])

        while index < len(self.nums) - 1 and self.nums[index] == self.nums[index + 1]:
            index += 1
        
        self.backtrack(index + 1, subset)
    

sln = Solution()
nums = [1,2,2]
print(sln.subsets(nums))