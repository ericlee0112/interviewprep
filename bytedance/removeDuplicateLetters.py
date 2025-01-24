'''
given string s, remove duplicate letters so that every letter appears once and only once. 
make sure that result is smallest in lexicographical order among all possible results

s = bcabc -> abc
s = cbacdcbc -> acdb

'''
import collections
def removeDuplicateLetters(s):
    lastOccurenceOfChars = collections.defaultdict(int)

    for i in range(len(s)):
        lastOccurenceOfChars[s[i]] = i
    
    stack = []
    seen = set()

    for i in range(len(s)):
        if s[i] in seen:
            continue

    
        while len(stack) > 0 and stack[-1] > s[i] and lastOccurenceOfChars[stack[-1]] > i:
            seen.remove(stack[-1])
            stack.pop()
            
        stack.append(s[i])
        seen.add(s[i])
    
    return "".join(stack)

s = "cbacdcbc"
print(removeDuplicateLetters(s))