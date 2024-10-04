'''
In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographically in this alien language.

 

Example 1:

Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
Example 2:

Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
Example 3:

Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character

'''

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # create alienDict
        alienDict = collections.defaultdict(int)
        for i in range(len(order)):
            alienDict[order[i]] = i
        
        for i in range(len(words) - 1):
            word = words[i]
            nextWord = words[i + 1]
            for j in range(len(word)):
                # if the length of the currentWord is greater than the next word, then it is not lexicographically sorted
                if j >= len(nextWord):
                    return False
                
                if word[j] != nextWord[j]:
                    # check hashmap
                    if alienDict[word[j]] > alienDict[nextWord[j]]:
                        return False
                    break
        return True

