'''
valid palindrome 2
Given a string s, return true if the s can be palindrome after deleting at most one character from it.
Example 1:

Input: s = "aba"
Output: true
Example 2:

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.
Example 3:

Input: s = "abc"
Output: false

'''

def validPalindrome(s):
    left = 0
    right = len(s) -1
    free = 1
    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        elif s[left] != s[right] and free > 0:
            free -= 1
            left += 1
            right -= 1
        else:
            return False
        
        
    return True

s = "abca"
print(validPalindrome(s))