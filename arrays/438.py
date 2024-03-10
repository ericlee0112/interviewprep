# find all anagrams in a string
# https://leetcode.com/problems/find-all-anagrams-in-a-string/description/
'''
Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Example 2:

Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".

soln: fixed length sliding window
compare window hashmap with p_hashmap
'''
import collections
def findAllAnagrams(s, p):
    if len(p) > len(s):
        return False

    # build p_hash
    p_hash = collections.defaultdict(int)
    for char in p:
        p_hash[char] += 1
    window_hash = collections.defaultdict(int)
    for i in range(len(p)):
        window_hash[s[i]] += 1
    
    left = 0
    right = len(p) - 1

    ans = []

    while right < len(s):
        # compare hashmaps
        if match(p_hash, window_hash):
            ans.append(left)
        
        window_hash[s[left]] -= 1
        left += 1
        right += 1
        if right < len(s):
            window_hash[s[right]] += 1
    return ans
    
def match(p_hash, window_hash):
    for char, freq in p_hash.items():
        if p_hash[char] != window_hash[char]:
            return False
    return True

s = "abab"
p = "ab"
print(findAllAnagrams(s,p))