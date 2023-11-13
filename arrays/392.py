# is subsequence
# https://leetcode.com/problems/is-subsequence/
"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) 
of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
"""
def isSubsequence(s,t):
    # two pointer 
    s_pointer = 0

    # loop through t
    for i in range(len(t)):
        # check t[i] matches s[0], if true, 
        if t[i] == s[s_pointer]:
            s_pointer += 1
    
    return s_pointer == len(s)

s = "ace"
t = "abcde"
print(isSubsequence(s,t))