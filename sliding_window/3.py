# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
'''
Given a string s, find the length of the longest
substring
without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

'''
import collections
class Solution:
    def lengthOfLongestSubstring(self, s):
        # use a hashmap to keep track of char frequencies in window
        max_window = 0
        left = 0
        right = 0 
        frequencies = collections.defaultdict(int)

        while right < len(s):
            frequencies[s[right]] += 1
            while frequencies[s[right]] > 1:
                left += 1
                frequencies[s[left]] -= 1
            right += 1
            max_window = max(max_window, right - left)
        return max_window

s = "abcabcbb"
sln = Solution()
print(sln.lengthOfLongestSubstring(s))
            
        