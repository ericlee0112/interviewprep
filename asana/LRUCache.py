import collections

class ListNode:
    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.forward = None
        self.backward = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.frontNode = ListNode(0)
        self.backNode = ListNode(0)
        self.frontNode.backward = self.backNode
        self.backNode.forward = self.frontNode
        
        self.hashmap = collections.defaultdict(ListNode)

    def get(self, key: int) -> int:
        if key in self.hashmap:
            node = self.hashmap[key]
            self.removeNode(node)
            self.putNodeAtFront(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            node = self.hashmap[key]
            node.val = value
            self.removeNode(node)
            self.putNodeAtFront(node)
        else:
            node = ListNode(key, value)
            self.hashmap[key] = node
            self.putNodeAtFront(node)
        
        if len(self.hashmap.keys()) > self.capacity:
            nodeToDelete = self.backNode.forward
            keyToDelete = nodeToDelete.key

            self.removeNode(self.backNode.forward)
            del(self.hashmap[keyToDelete])
    
    def putNodeAtFront(self, node):
        previousFirstNode = self.frontNode.backward
        self.frontNode.backward = node
        node.forward = self.frontNode

        previousFirstNode.forward = node
        node.backward = previousFirstNode
        
    
    def removeNode(self, node): 
        nodeInFront = node.forward
        nodeInBack = node.backward
        nodeInFront.backward = nodeInBack
        nodeInBack.forward = nodeInFront



        