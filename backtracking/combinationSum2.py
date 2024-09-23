'''
https://neetcode.io/problems/combination-target-sum-ii

You are given an array of integers candidates, which may contain duplicates, and a target integer target. 
Your task is to return a list of all unique combinations of candidates where the chosen numbers sum to target.

Each element from candidates may be chosen at most once within a combination. The solution set must not contain duplicate combinations.

You may return the combinations in any order and the order of the numbers in each combination can be in any order.

Example 1:

Input: candidates = [9,2,2,4,6,1,5], target = 8

Output: [
  [1,2,5],
  [2,2,4],
  [2,6]
]
Example 2:

Input: candidates = [1,2,3,4,5], target = 7

Output: [
  [1,2,4],
  [2,5],
  [3,4]
]

'''

class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        self.memo = set()
        self.candidates = candidates
        self.target = target

        self.ans = []
        self.traverse(0, [])

        return self.ans
    
    def traverse(self, index, combination):
        print([index, combination])
        if sum(combination) == self.target and str(combination) not in self.memo:
            self.memo.add(str(combination))
            self.ans.append(combination)
        elif index < len(self.candidates) and sum(combination) < self.target:
            for i in range(index, len(self.candidates)):
                if i > index and self.candidates[i] == self.candidates[i - 1]:
                    continue
                self.traverse(i + 1, combination + [self.candidates[i]])