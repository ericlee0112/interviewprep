'''
https://leetcode.com/problems/minimum-window-substring/description/

Given two strings s and t of lengths m and n respectively, return the minimum window 
substring
 of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
'''

import collections
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window_hashmap = collections.defaultdict(int)
        t_hashmap = collections.defaultdict(int)

        result_indices = [0,0]
        result_length = float('inf')

        for char in t:
            t_hashmap[char] += 1

        need = len(t_hashmap.keys())
        have = 0

        left = 0

        for right in range(len(s)):
            char = s[right]
            window_hashmap[char] += 1

            if t_hashmap[char] == window_hashmap[char]:
                have += 1

            # while all char frequency requirements have been met
            while have == need:
                # update result indices
                if (right - left + 1) < result_length:
                    result_length = right - left + 1
                    result_indices = [left, right]
                
                # start shaving from left
                window_hashmap[s[left]] -= 1
                # update have
                if window_hashmap[s[left]] < t_hashmap[s[left]]:
                    have -= 1
                left += 1
        
        if result_length == float('inf'):
            return ""
        else:
            return s[result_indices[0] : result_indices[1] + 1]


s = "ADOBECODEBANC"
t = "ABC"

sln = Solution()
print(sln.minWindow(s,t))