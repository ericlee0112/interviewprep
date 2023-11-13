'''
Design Dynamic Array (Resizable Array)
Design a Dynamic Array (aka a resizable array) class, such as an ArrayList in Java or a vector in C++.

Your DynamicArray class should support the following operations:

DynamicArray(int capacity) will initialize an empty array with a capacity of capacity, where capacity > 0.
int get(int i) will return the element at index i. Assume that index i is valid.
void set(int i, int n) will set the element at index i to n. Assume that index i is valid.
void pushback(int n) will push the element n to the end of the array.
int popback() will pop and return the element at the end of the array. Assume that the array is non-empty.
void resize() will double the capacity of the array.
int getSize() will return the number of elements in the array.
int getCapacity() will return the capacity of the array.
If we call void pushback(int n) but the array is full, we should resize the array first.

Example 1:

Input:
["Array", 1, "getSize", "getCapacity"]

Output:
[null, 0, 1]
Example 2:

Input:
["Array", 1, "pushback", 1, "getCapacity", "pushback", 2, "getCapacity"]

Output:
[null, null, 1, null, 2]
Example 3:

Input:
["Array", 1, "getSize", "getCapacity", "pushback", 1, "getSize", "getCapacity", "pushback", 2, "getSize", "getCapacity", "get", 1, "set", 1, 3, "get", 1, "popback", "getSize", "getCapacity"]

Output:
[null, 0, 1, null, 1, 1, null, 2, 2, 2, null, 3, 3, 1, 2]

'''

class DynamicArray:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.array = []
        self.nextSpot = 0

    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        self.array[i] = n

    def pushback(self, n: int) -> None:
        if len(self.array) == self.capacity:
            self.resize()
            
        self.array.append(n)
        self.nextSpot += 1

    def popback(self) -> int:
        popped = self.array[self.nextSpot - 1]
        del(self.array[self.nextSpot - 1])
        self.nextSpot -= 1
        return popped
 
    def resize(self) -> None:
        self.capacity += self.capacity

    def getSize(self) -> int:
        return len(self.array)
    
    def getCapacity(self) -> int:
        return self.capacity
    
dynamicArray = DynamicArray(3)
# ["Array", 3, "pushback", 1, "pushback", 2, "pushback", 3, "get", 0, "get", 1, "get", 2]
dynamicArray.pushback(1)
dynamicArray.pushback(2)
dynamicArray.pushback(3)
dynamicArray.get(0)
dynamicArray.get(1)
dynamicArray.get(2)



