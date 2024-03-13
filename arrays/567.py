'''
permutation in string https://leetcode.com/problems/permutation-in-string/description/

Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

 

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false

'''
import collections
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_hash = collections.defaultdict(int)
        for char in s1:
            s1_hash[char] += 1
        
        n = len(s1)
        window_hash = collections.defaultdict(int)
        for i in range(n):
            window_hash[s2[i]] += 1
        

        left = 0
        right = n - 1
        while right < len(s2):
            # compare hashmaps
            if self.match(s1_hash, window_hash):
                return True

            window_hash[s2[left]] -= 1
            left += 1
            right += 1
            if right < len(s2):
                window_hash[s2[right]] += 1
        return False
    
    def match(self, s1_hash, window_hash):
        for char, freq in s1_hash.items():
            if window_hash[char] != freq:
                return False
        return True


s1 = "ab"
s2 = "eidboaoo"
print(checkInclusion(s1,s2))