import collections

class TrieNode:
    def __init__(self, char):
        self.char = char
        self.end = False
        self.children = collections.defaultdict(TrieNode)


class PrefixTree:
    def __init__(self):
        self.parentNode = TrieNode("")

    def insert(self, word: str) -> None:
        if len(word) == 0:
            return
        
        firstChar = word[0]
        if firstChar not in self.parentNode.children:
            trienode = TrieNode(firstChar)
            self.parentNode.children[firstChar] = trienode
            self.insertChar(word, 1, trienode)
        else:
            self.insertChar(word, 1, self.parentNode.children[firstChar])
    
    def insertChar(self, word, index, parentNode):
        if index == len(word):
            parentNode.end = True
            return

        if index < len(word):
            char = word[index]
            if char not in parentNode.children:
                childNode = TrieNode(char)
                parentNode.children[char] = childNode
            else:
                childNode = parentNode.children[char]
            self.insertChar(word, index + 1, childNode)

    def search(self, word: str) -> bool:
        if len(word) == 0:
            return True

        firstChar = word[0]
        if firstChar in self.parentNode.children:
            res = self.searchChar(word, 1, self.parentNode.children[word[0]])
            return res
        else:
            return False

    
    def searchChar(self, word, index, parentNode):
        if index == len(word):
            return parentNode.end
        
        if index < len(word):
            char = word[index]
            if char not in parentNode.children:
                return False
            else:
                childNode = parentNode.children[char]
                return self.searchChar(word, index + 1, childNode)   

    def startsWith(self, prefix: str) -> bool:
        if prefix == "":
            return True

        firstChar = prefix[0]
        if firstChar in self.parentNode.children:
            res = self.searchPrefix(prefix, 1, self.parentNode.children[firstChar])
            return res
        else:
            return False
    
    def searchPrefix(self, prefix, index, parentNode):
        if index == len(prefix):
            return True
            
        if index < len(prefix):
            char = prefix[index]
            if char not in parentNode.children:
                return False
            else:
                childNode = parentNode.children[char]
                return self.searchPrefix(prefix, index + 1, childNode)   
            
    
        
        