#https://leetcode.com/problems/word-pattern/description/
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern_hashmap = collections.defaultdict(str)
        s_hashmap = collections.defaultdict(str)
        
        new_s = s.split(" ")

        if len(new_s) != len(pattern):
            return False

        for i in range(len(new_s)):
            if new_s[i] not in s_hashmap and pattern[i] not in pattern_hashmap:
                s_hashmap[new_s[i]] = pattern[i]
                pattern_hashmap[pattern[i]] = new_s[i]
            elif s_hashmap[new_s[i]] != pattern[i] or pattern_hashmap[pattern[i]] != new_s[i]:
                return False
       
        
        return True
