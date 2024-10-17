class TrieNode:
    def __init__(self, char):
        self.char = char
        self.children = collections.defaultdict(TrieNode)
        self.end = False
    
    def insertWord(self, word):
        if word[0] not in self.children:
            node = TrieNode(word[0])
            self.children[word[0]] = node
        else:
            node = self.children[word[0]]
        self.insertChar(node, word, 1)
    
    def insertChar(self, parentNode, word, i):
        if i == len(word):
            parentNode.end = True
            return
        char = word[i]
        if char in parentNode.children:
            node = parentNode.children[char]
        else:
            node = TrieNode(char)
            parentNode.children[char] = node
        
        self.insertChar(node, word, i + 1)
    
    def findWord(self, word):
        if word[0] not in self.children:
            return False
        node = self.children[word[0]]
        return self.findChar(node, word, 1)
    
    def findChar(self, parentNode, word, i):
        if i == len(word):
            return parentNode.end
        char = word[i]
        if char not in parentNode.children:
            return False
        node = parentNode.children[char]
        self.findChar(node, word, i + 1)

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        node = TrieNode("")
        for word in wordDict:
            node.insertWord(word)
        
        self.dp = [False for _ in range(len(s) + 1)]
        self.dp[0] = True
        for i in range(len(s)):
            if self.dp[i]:
                self.searchTrie(node, s, i)

        return self.dp[-1]
    
    def searchTrie(self, node, s, i):
        currentNode = node
        for j in range(i, len(s)):
            if s[j] in currentNode.children:
                currentNode = currentNode.children[s[j]]
                if currentNode.end:
                    self.dp[j + 1] = True
            else:
                break
