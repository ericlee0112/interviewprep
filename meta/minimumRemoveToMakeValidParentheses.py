'''
given a string s of (, ), and lowercase letters

remove minimum number of parentheses in any positions so that the resulting string is valid 

parentheses string is valid if and only if :
    - it is the empty string, contains only lowercase characters
    - it can be written as AB
    - it can be written as (A)


e.g.
Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.

'''
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        leftBrackets = 0
        rightBrackets = 0
        s = list(s)

        for i in range(len(s)):
            if s[i] == '(':
                leftBrackets += 1
            elif s[i] == ')':
                if leftBrackets > rightBrackets:
                    rightBrackets += 1
                else:
                    s[i] = "*"
    
        
        if leftBrackets > rightBrackets:

            leftBrackets = 0
            rightBrackets = 0
            for i in range(len(s) - 1, -1, -1):
                if s[i] == ")":
                    rightBrackets += 1
                elif s[i] == "(":
                    if rightBrackets > leftBrackets:
                        leftBrackets += 1
                    else:
                        s[i] = "*"

        new_s = ""
        for char in s:
            if char != "*":
                new_s += char
        return new_s
