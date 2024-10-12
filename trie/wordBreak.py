class TrieNode:
    def __init__(self, char):
        self.char = char
        self.children = collections.defaultdict(TrieNode)
        self.end = False
    
    def insertWord(self, word):
        if word[0] in self.children:
            node = self.children[word[0]]
        else:
            node = TrieNode(word[0])
            self.children[word[0]] = node
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
        char = word[o]
        if char not in self.children:
            return False
        node = self.children[word[0]]
        res = self.findChar(node, word, 1)
        return res

    def findChar(self, parentNode, word, i):
        if i == len(word):
            return parentNode.end

        char = word[i]
        if char not in parentNode.children:
            return False
      
        childNode = parentNode.children[char]
        return self.findChar(word, i + 1, childNode)   



class Solution:
    def wordBreak(self, s, words):
        node = TrieNode("")
        self.dp = [False for _ in range(len(s) + 1)]
        self.dp[0] = True

        for word in words:
            node.insertWord(word)
        
        for i in range(len(s)):
            if self.dp[i]:
                self.searchTrie(node, s, i)
            
        return self.dp[-1]

    def searchTrie(self, node, s, i):
        currentNode = node
        for i in range(i, len(s)):
            if s[i] in currentNode.children:
                currentNode = currentNode.children[s[i]]
                if currentNode.end:
                    self.dp[i + 1] = True
            else:
                break

    