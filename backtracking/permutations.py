'''
Given an array nums of unique integers, return all the possible permutations. You may return the answer in any order.

Example 1:

Input: nums = [1,2,3]

Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

'''
class Solution:
    def permute(self, nums):
        self.size = len(nums)
        self.ans = []

        self.buildPermutation(nums, [])

        return self.ans
        
    
    def buildPermutation(self, numsRemaining, permutation):
        if len(permutation) == self.size:
            self.ans.append(permutation)
            return

        for i in range(len(numsRemaining)):
            # traverse
            numToPull = numsRemaining[i]
            self.buildPermutation(numsRemaining[:i] + numsRemaining[i + 1:], permutation + [numToPull])
        
sln = Solution()
res = sln.permute([1,2,3])
print(res)