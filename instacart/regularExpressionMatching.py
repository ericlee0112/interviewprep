'''
Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where:

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

 

Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input: s = "aa", p = "*"
Output: true
Explanation: '*' matches any sequence.
Example 3:

Input: s = "cb", p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'
'''
import collections

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        self.s = s
        self.p = p
        self.cache = collections.defaultdict(int)
        return self.dfs(0,0)
        
    def dfs(self, i, j):
        if (i,j) in self.cache:
            return self.cache[(i,j)]
        if i >= len(self.s) and j >= len(self.p):
            return True
        if j >= len(self.p):
            return False
        
        if i < len(self.s) and (self.s[i] == self.p[j] or self.p[j] == '.'):
            charMatch = True
        else:
            charMatch = False
        
        if (j + 1) < len(self.p) and self.p[j + 1] == '*':
            # explore both options
            res = self.dfs(i, j + 2) or (charMatch and self.dfs(i + 1, j))
            self.cache[(i,j)] = res
            return res
        
        if charMatch:
            res = self.dfs(i + 1, j + 1)
            self.cache[(i,j)] = res
            return res
        else:
            self.cache[(i,j)] = False
            return False
                
