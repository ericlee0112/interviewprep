'''
Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences in any order.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

 

Example 1:

Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
Output: ["cats and dog","cat sand dog"]
Example 2:

Input: s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]
Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
Explanation: Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: []
'''

        
class Solution:
    def wordBreak(self, s: str, wordDict):

        self.wordSet = set(wordDict)
        self.s = s

        self.ans = []
        self.findSentence(0, "", [])

        return self.ans

    # indx
    def findSentence(self, index, word, sentence):
        if index == len(self.s):
            if word in self.wordSet:
                sentence.append(word)
                self.ans.append(" ".join(sentence))
            return
        if word in self.wordSet:
            self.findSentence(index + 1, self.s[index], sentence + [word])
        
        self.findSentence(index + 1, word + self.s[index], sentence)