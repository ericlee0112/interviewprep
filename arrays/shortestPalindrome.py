# given string s, you can convert s to a palindrome by adding characters in front of it 
# return the shortest possible palindrome you can find by performing this operation
'''
Example 1:
Input: s = "aacecaaa"
Output: "aaacecaaa"

s = "aacecaaa"
t = "aaacecaa"


Example 2:
Input: s = "abcd"
Output: "dcbabcd"


ex: 
s = "abcd"
t = "dcba"
res = dcbabcd
'''

def shortestPalindrome(s):
    # string t is reversed(s)
    t = ""
    for i in range(len(s) - 1, -1, -1):
        t += s[i]

    for i in range(len(t)):
        t_suffix = t[i:]
        t_prefix = t[:i]
        if s.startswith(t_suffix):
            return t_prefix + s
    
    return t + s

s = "aacecaaa"
print(shortestPalindrome(s))
