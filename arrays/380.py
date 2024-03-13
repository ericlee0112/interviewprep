# insert delete getrandom o(1)
'''
https://leetcode.com/problems/insert-delete-getrandom-o1/description/
Implement the RandomizedSet class:

RandomizedSet() Initializes the RandomizedSet object.
bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
You must implement the functions of the class such that each function works in average O(1) time complexity.

 

Example 1:

Input
["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
[[], [1], [2], [2], [], [1], [2], []]
Output
[null, true, false, true, 2, true, false, 2]

Explanation
RandomizedSet randomizedSet = new RandomizedSet();
randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomizedSet.remove(2); // Returns false as 2 does not exist in the set.
randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now contains [1,2].
randomizedSet.getRandom(); // getRandom() should return either 1 or 2 randomly.
randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now contains [2].
randomizedSet.insert(2); // 2 was already in the set, so return false.
randomizedSet.getRandom(); // Since 2 is the only number in the set, getRandom() will always return 2.
 
'''
import random
import collections
class RandomizedSet:
    def __init__(self):
        self.index_to_val = collections.defaultdict(int) 
        self.val_to_index = collections.defaultdict(int) 
        self.index = 0

    def insert(self, val):
        if val not in self.val_to_index:
            self.val_to_index[val] = self.index
            self.index_to_val[self.index] = val
            self.index += 1

            return True
        return False

    def remove(self, val):
        if val in self.val_to_index:
            index = self.val_to_index[val]
            del(self.val_to_index[val])
            del(self.index_to_val[index])            

            return True
        return False

    def getRandom(self):
        list_of_indexes = list(self.index_to_val.keys())
        randomIndex = random.randint(0, len(self.index_to_val) - 1)
        index = list_of_indexes[randomIndex]
        return self.index_to_val[index]
    
randomizedSet = RandomizedSet()
randomizedSet.insert(1)
randomizedSet.remove(2)
randomizedSet.insert(2)
randomizedSet.getRandom()
randomizedSet.remove(1)
randomizedSet.insert(2)
randomizedSet.getRandom()