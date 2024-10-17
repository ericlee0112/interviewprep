# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

import collections

class Solution:
    def pivotIndex(self, nums):
        leftSum = [0 for _ in range(len(nums))]
        leftSum[0] = nums[0]

        rightSum = [0 for _ in range(len(nums))]
        rightSum[-1] = nums[-1]
        
        for i in range(1, len(nums)):
            leftSum[i] = leftSum[i - 1] + nums[i]
        
        for i in range(len(nums) - 2, -1, -1):
            rightSum[i] = rightSum[i + 1] + nums[i]
        
        for i in range(len(leftSum)):
            if leftSum[i] == rightSum[i]:
                return i
        
        return -1

    def minWindow(self, s, t):

        window_hashmap = collections.defaultdict(int)
        t_hashmap = collections.defaultdict(int)

        for char in t:
            t_hashmap[char] += 1
        
        have = 0
        need = len(t_hashmap.keys())

        result_indices = [-1, -1]
        result_length = 10000000

        left = 0
        for right in range(len(s)):
            char = s[right]
            window_hashmap[char] += 1

            if char in t_hashmap and t_hashmap[char] == window_hashmap[char]:
                have += 1
            
            # if all character frequency requirements have been met
            while have == need:
                
                # update result_indices and result_length
                if (right - left + 1) < result_length:
                    result_length = (right - left + 1)
                    result_indices = [left, right]
                
                # start shaving from the left
                window_hashmap[s[left]] -= 1
                if s[left] in t_hashmap and window_hashmap[s[left]] < t_hashmap[s[left]]:
                    have -= 1
                left += 1 

        if result_length == 10000000:
            return ""
        else:
            l = result_indices[0]
            r = result_indices[1]
            return s[l:r+1]
    
    def generateParenthesis(self, n):
        self.parentheses = []
        self.generate(n,n, "")
        return self.parentheses
    
    def generate(self, left, right, s):
        if left == 0 and right == 0:
            self.parentheses.append(s)
        elif left == 0:
            self.generate(left, right - 1, s + ")")
        elif left == right:
            self.generate(left-1,right, s + "(")
        else:
            self.generate(left, right - 1, s + ")")
            self.generate(left - 1, right, s + "(")

s = "ADOBECODEBANC"
t = "ABC"

nums = [1,7,3,6,5,6]

sln = Solution()

print(sln.generateParenthesis(3))