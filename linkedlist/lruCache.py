import collections 

class ListNode:
    def __init__(self, val):
        self.val = val
        self.key = None
        self.forward = None
        self.backward = None

class LRUCache:
    def __init__(self, capacity):
        self.hashmap = collections.defaultdict(int)
        self.capacity = capacity
        self.first = ListNode(0)
        self.last = ListNode(0)
        self.first.backward = self.last
        self.last.forward = self.first

    def insert(self, node):
        previous = self.first.backward

        self.first.backward = node
        node.forward = self.first

        previous.forward = node
        node.backward = previous

    
    def remove(self, node):
        previous = node.backward
        nextNode = node.forward
        previous.forward = nextNode
        nextNode.backward = previous
        
    def get(self, key):
        if key not in self.hashmap:
            return -1
        self.remove(self.hashmap[key])
        self.insert(self.hashmap[key])
        return self.hashmap[key].val   

    def put(self, key, val):
        node = ListNode(val)
        node.key = key
        if key in self.hashmap:
            self.hashmap[key].val = val
            self.remove(self.hashmap[key])
        else:
            self.hashmap[key] = node
            # put node at the top
        self.insert(self.hashmap[key])

        if len(self.hashmap.keys()) > self.capacity:
            # remove last
            lruNode = self.last.forward
            self.remove(lruNode)
            del(self.hashmap[lruNode.key])
        
        
