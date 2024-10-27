import collections


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head):
        if head is None:
            return None
        
        # create map that maps old node to copy
        originalToCopy = collections.defaultdict(Node)
        curr = head
        while curr is not None:
            copy = Node(curr.val)
            originalToCopy[curr] = copy
            curr = curr.next
        
        curr = head
        while curr is not None:
            copyNode = originalToCopy[curr]
            if curr.next is not None:
                nextNodeCopy = originalToCopy[curr.next]
                copyNode.next = nextNodeCopy
            if curr.random is not None:
                randomNodeCopy = originalToCopy[curr.random]
                copyNode.random = randomNodeCopy
            curr = curr.next
        
        return originalToCopy[head]
    