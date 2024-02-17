# https://leetcode.com/problems/longest-repeating-character-replacement/
'''
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.
'''
import collections
class Solution:
    def characterReplacement(self, s, k):
        max_length = 0
        # use hashmap to keep track of char frequences in the sliding window
        # rule: window length - hashmap[most frequent char] >= k
        # if rule is satisfied, expand window
        # else, shrink window until rule is satisfied
        frequencies = collections.defaultdict(int)
        left = 0
        right = 0
        while right < len(s):
            frequencies[s[right]] += 1
            if (right - left + 1) - (max(frequencies.values())) <= k:
                right += 1
            else:
                while (right - left + 1) - (max(frequencies.values())) > k:
                    frequencies[s[left]] -= 1
                    left += 1
                right += 1
                    
            max_length = max(max_length, right - left)
        return max_length


                    
                

    
s = "AABABBA"
k = 1

sln = Solution()
print(sln.characterReplacement(s,k))
        
        

