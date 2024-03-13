'''
repeated dna sequences
https://leetcode.com/problems/repeated-dna-sequences/description/
The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.

For example, "ACGAATTCCG" is a DNA sequence.
When studying DNA, it is useful to identify repeated sequences within the DNA.

Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule. You may return the answer in any order.

 

Example 1:

Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC","CCCCCAAAAA"]
Example 2:

Input: s = "AAAAAAAAAAAAA"
Output: ["AAAAAAAAAA"]

'''
import collections

def findRepeatedDnaSequences(s):
    if len(s) < 10:
        return []
    hashmap = collections.defaultdict(int)
    # sliding window of size 10 
    # left position starts at 0
    left = 0
    # right at 9
    right = 9
    
    # while right < len(s)
    while right < len(s):
        # get the substring at s[left:right+1]
        sequence = s[left:right + 1]
        # add substring to hashmap
        hashmap[sequence] += 1
        left += 1
        right += 1
    
    ans = []
    for seq, freq in hashmap.items():
        if freq > 1:
            ans.append(seq)
    
    return ans

s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
print(findRepeatedDnaSequences(s))
    
