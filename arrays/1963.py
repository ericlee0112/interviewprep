'''
minimum number of swaps to make string balanced

why maxClosingBrackets +  1 // 2 ? 

example:
]]][[[[]

3 extra closing brackets 

after one swap, we go from 3 extra closing brackets to 1 extra closing bracket
[]][[][]
one more swap, and we go from 1 extra closing bracket to 0 extra closing brackets

'''
import collections
def minSwaps(s):
    s = list(s)   
    
    maxClosingBrackets = 0
    extraClosingBrackets = 0
    for i in range(len(s)):
        if s[i] == ']':
            extraClosingBrackets += 1
        else:
            extraClosingBrackets -= 1
        maxClosingBrackets = max(maxClosingBrackets, extraClosingBrackets )
    return (maxClosingBrackets + 1) // 2

s = "]]][[["
print(minSwaps(s))