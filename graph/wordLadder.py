'''
word ladder


'''
import collections

def ladderLength(beginWord, endWord, wordList):
    chars = ['a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    wordList = set(wordList)
    queue = collections.deque([(beginWord, 1)])
    while len(queue) > 0:
        word, distance = queue.popleft()
        if word == endWord:
            return distance
        # generate new word
        for i in range(len(word)):
            for char in chars:
                newWord = word[:i] + char + word[i + 1:]
                if newWord in wordList:
                    wordList.remove(newWord)
                    queue.append((newWord, distance + 1))
    return 0

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
print(ladderLength(beginWord, endWord, wordList))