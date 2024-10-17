class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = collections.defaultdict(int)
        l = 0
        r = 0

        longestSubstring = 0

        while r < len(s):
            if hashmap[s[r]] == 0:
                hashmap[s[r]] += 1
                longestSubstring = max(longestSubstring, r - l + 1)
                r += 1
            else:
                while l < r and hashmap[s[r]] >= 1:
                    hashmap[s[l]] -= 1
                    l += 1



        return longestSubstring