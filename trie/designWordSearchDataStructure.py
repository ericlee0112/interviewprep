import collections

class TrieNode:
    def __init__(self, char):
        self.char = char
        self.end = False
        self.children = collections.defaultdict(TrieNode)


class WordDictionary:
    def __init__(self):
        self.parentNode = TrieNode("")

    def addWord(self, word):
        if word[0] not in self.parentNode.children:
            # add 
            newNode = TrieNode(word[0])
            self.parentNode.children[word[0]] = newNode
            self.addChar(newNode, 1, word)
        else:
            node = self.parentNode.children[word[0]]
            self.addChar(node, 1, word)
            
    
    def addChar(self, parentNode, index, word):
        if index == len(word):
            return
        char = word[index]
        if char in parentNode.children:
            node = parentNode.children[char]
        else:
            node = TrieNode(char)
            parentNode.children[char] = node
        self.addChar(node, index + 1, word)
    
    def search(self, word):
        if word[0] == '.':
            # search all children nodes
            for char, node in self.parentNode.children.items():
                res = self.searchChar(node, 1, word)
                if res:
                    return True
            return False

        elif word[0] in self.parentNode.children:
            node = self.parentNode.children[word[0]]
            res = self.searchChar(node, 1, word)
            return res
        else:
            return False


    def searchChar(self, parentNode, index, word):
        if index == len(word):
            return True

        if word[index] == '.':
            for char, node in parentNode.children.items():
                res = self.searchChar(node, index + 1, word)
                if res:
                    return True
                
            return False 
        
        elif word[index] in parentNode.children:
            node = parentNode.children[word[index]]
            return self.searchChar(node, index + 1, word)
        else:
            return False
